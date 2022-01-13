from otree.api import *
# from django.contrib.messages import get_messages

c = Currency  # old name for currency; you can delete this.


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1
    endowment = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    submit_missing = models.IntegerField(initial=0)
    age = models.IntegerField(label='What is your age?', min=13, max=125, blank=True)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'], ['Other', 'Other']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
     blank = True
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

# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', "income"]

    @staticmethod
    def js_vars(player):    # highlights variables/fields that do not need to be filled (but that we'll be displaying a one-time warning message if they're left blank)
        return dict(optional_fields = Demographics.form_fields[2:4],
                    required_fields = Demographics.form_fields[0:2])
    pass



page_sequence = [Demographics]