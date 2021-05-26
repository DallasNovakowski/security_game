from otree.api import *
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
    prolific_id = models.StringField(default=str(" "))
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
    )



# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'education', "income"]

    @staticmethod
    def before_next_page(self, timeout_happened):
        self.prolific_id = self.participant.label
    pass

class Task_intro(Page):
    form_model = 'player'
    pass

page_sequence = [Demographics, Task_intro]
