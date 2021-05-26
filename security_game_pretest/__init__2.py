from otree.api import *

c = Currency

doc = """
This app is designed as a pretest of the security game stimuli - namely manupulating 
amount stolen, base probability of theft, and security price/efficacy
"""


class Constants(BaseConstants):
    name_in_url = 'security_game_pretest'
    players_per_group = None
    num_rounds = 1
    security_efficacy = .01
    security_price_04 = .04
    base_theft_success_50 = .5
    endowment = 2
    security_price_02 = .02
    base_theft_success_75 = .75
    failed_attack = 1
    base_theft_success_60 = .6
    lost_from_attacks = 1



class Player(BasePlayer):
    age = models.IntegerField(label="What is your age?")
    gender = models.StringField(label="What is your gender?",
                                choices=[["Male", "Male"], ["Female", "Female"], ["Other", "Other"]])
    security_consumed = models.CurrencyField(label="How much security would you like to purchase?", min=0)
    security_consumed_50_04 = models.CurrencyField(label="How much security would you like to purchase?", min=0, max=25)
    security_consumed_50_02 = models.CurrencyField(label="How much security would you like to purchase?", min=0, max=50)
    security_consumed_60_04 = models.CurrencyField(label="How much security would you like to purchase?", min=0, max=25)
    security_consumed_60_02 = models.CurrencyField(label="How much security would you like to purchase?", min=0, max=50)
    security_consumed_75_02 = models.CurrencyField(label="How much security would you like to purchase?", min=0, max=50)
    security_consumed_75_04 = models.CurrencyField(label="How much security would you like to purchase?", min=0, max=25)
    pass


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# PAGES
class Demo(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']
    pass


class Intro(Page):
    form_model = 'player'
    pass


class PreTest50_04(Page):
    form_model = 'player'
    form_fields = ['security_consumed_50_04']

    @staticmethod
    def js_vars(player):
        return dict(
            efficacy=Constants.security_efficacy,
            endowment=Constants.endowment,
            price=Constants.security_price_04,
            theft_success=Constants.base_theft_success_50,
            lost_from_attacks=Constants.lost_from_attacks,
            failed_attack=Constants.failed_attack,
        )
    pass

class PreTest50_02(Page):
    form_model = 'player'
    form_fields = ['security_consumed_50_02']

    @staticmethod
    def js_vars(player):
        return dict(
            efficacy=Constants.security_efficacy,
            endowment=Constants.endowment,
            price=Constants.security_price_02,
            theft_success=Constants.base_theft_success_50,
            lost_from_attacks=Constants.lost_from_attacks,
            failed_attack=Constants.failed_attack,
        )
    pass

class PreTest60_04(Page):
    form_model = 'player'
    form_fields = ['security_consumed_60_04']

    @staticmethod
    def js_vars(player):
        return dict(
            efficacy=Constants.security_efficacy,
            endowment=Constants.endowment,
            price=Constants.security_price_04,
            theft_success=Constants.base_theft_success_60,
            lost_from_attacks=Constants.lost_from_attacks,
            failed_attack=Constants.failed_attack,
        )
    pass

class PreTest60_02(Page):
    form_model = 'player'
    form_fields = ['security_consumed_60_02']

    @staticmethod
    def js_vars(player):
        return dict(
            efficacy=Constants.security_efficacy,
            endowment=Constants.endowment,
            price=Constants.security_price_02,
            theft_success=Constants.base_theft_success_60,
            lost_from_attacks=Constants.lost_from_attacks,
            failed_attack=Constants.failed_attack,
        )
    pass

class PreTest75_04(Page):
    form_model = 'player'
    form_fields = ['security_consumed_75_04']

    @staticmethod
    def js_vars(player):
        return dict(
            efficacy=Constants.security_efficacy,
            endowment=Constants.endowment,
            price=Constants.security_price_04,
            theft_success=Constants.base_theft_success_75,
            lost_from_attacks=Constants.lost_from_attacks,
            failed_attack=Constants.failed_attack,
        )
    pass

class PreTest75_02(Page):
    form_model = 'player'
    form_fields = ['security_consumed_75_02']

    @staticmethod
    def js_vars(player):
        return dict(
            efficacy=Constants.security_efficacy,
            endowment=Constants.endowment,
            price=Constants.security_price_02,
            theft_success=Constants.base_theft_success_75,
            lost_from_attacks=Constants.lost_from_attacks,
            failed_attack=Constants.failed_attack,
        )
    pass



page_sequence = [PreTest50_04, PreTest50_02, PreTest60_04, PreTest60_02, PreTest75_04, PreTest75_02]
