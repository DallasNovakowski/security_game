from otree.api import *
# from django.contrib.messages import get_messages

c = Currency  # old name for currency; you can delete this.


class Constants(BaseConstants):
    name_in_url = 'intro'
    players_per_group = None
    num_rounds = 1
    endowment = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    submit_missing = models.IntegerField(initial=0)
    prolific_id = models.StringField(default=str(""))
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'], ['Other', 'Other']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    education = models.StringField(
        choices = ['Less than high school degree', "High school graduate (high school diploma or equivalent including GED)",
                   "Some college but no degree",  "Associate degree in college (2-year)", "Bachelor's degree in college (4-year)",
                   "Master's degree", "Doctoral degree", "Professional degree (JD, MD)"],
        label = 'What is the highest level of school you have completed or the highest degree you have received?',
        widget = widgets.RadioSelect,
        blank=True
    )
    income = models.StringField(
        choices=["Less than $10,000", "$10,000 to $19,999", "$20,000 to $29,999", "$30,000 to $39,999", "$40,000 to $49,999",
                 "$50,000 to $59,999",
                 "$60,000 to $69,999",
                 "$70,000 to $79,999",
                 "$80,000 to $89,999",
                 "$90,000 to $99,999",
                 "$100,000 to $149,999",
                 "$150,000 or more"],
        label='Please indicate the answer that includes your entire household income over the previous year (in USD) before taxes.',
        widget=widgets.RadioSelect,
        blank=True
    )
    ts_demo = models.FloatField(blank=True)
    ts_intro = models.FloatField(blank=True)


# functions
# def get_response_data():
#     return [
#         dict(
#             name='age',
#             explanation="did you answer everything you needed to?.",
#         ),
#         dict(
#             name='education',
#             explanation="did you answer everything you needed to?. But better?",
#         ),
#     ]

# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', "income", 'ts_demo']



    @staticmethod
    def js_vars(player):    # highlights variables/fields that do not need to be filled (but that we'll be displaying a one-time warning message if they're left blank)
        return dict(optional_fields = Demographics.form_fields[2:4],
                    required_fields = Demographics.form_fields[0:2])
    pass

    # @staticmethod
    # def vars_for_template(player: Player):
    #     fields = get_response_data()
    #     for d in fields:
    #         d['is_correct'] = not getattr(player,  d['name'])
    #         return dict(fields=fields, show_solutions=True)

    #
    # @staticmethod
    # def message(player: Player, values):
    #     # since 'values' is a dict, yo[u could also do sum(values.values())
    #     if ['age'] != 100:
    #         return 'Numbers must add up to 100'

    # messages.add_message(request, messages.INFO, 'Hello world.')

    #
    # @staticmethod
    # def mess(player, values):
    #     form_fields = dict(
    #         quiz1=42,
    #         quiz2='Ottawa',
    #         quiz3='3.14',
    #         quiz4='George Washington'
    #     )
    #
    #     message = dict()
    #
    #     for field_name in form_fields:
    #         if not values[field_name]:
    #             message[field_name] = 'Wrong answer'
    #
    #     return message



    # @staticmethod
    # def done(request):
    #     template = loader.get_template('maps/done.html')
    #
    # context = RequestContext(request, {
    #     'reports_link': report_array, // I
    # believe
    # this is not correct.
    # })
    # pass



class Task_intro(Page):
    form_model = 'player'
    form_fields = ['ts_intro']


    @staticmethod
    def before_next_page(self, timeout_happened):
        self.prolific_id = self.participant.label
    pass

page_sequence = [Demographics, Task_intro]
