from otree.api import *

c = Currency

doc = """
This app is a basic sample of the security game
"""


class Constants(BaseConstants):
    name_in_url = 'security_game'
    players_per_group = None
    num_rounds = 1
    security_efficacy = .02
    security_price = .04
    base_theft_success = .6
    lost_from_attacks = 1
    endowment = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label="What is your age?")
    gender = models.StringField(label="What is your gender?",
                                choices=[["Male", "Male"], ["Female", "Female"], ["Other", "Other"]])
    security_consumed = models.CurrencyField(label="How much security would you like to purchase?", min=0)
    pass


# PAGES
class Demo(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']
    pass


class Intro(Page):
    form_model = 'player'
    pass


class SampleGame(Page):
    form_model = 'player'
    form_fields = ['security_consumed']

    @staticmethod
    def js_vars(player):
        return dict(
            efficacy=Constants.security_efficacy,
            price=Constants.security_price,
            theft_success=Constants.base_theft_success,
            endowment=Constants.endowment
        )
    pass


page_sequence = [SampleGame]
