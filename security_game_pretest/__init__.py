from otree.api import *

import random

from otree.models import player

c = Currency

doc = """
This app is designed as a pretest of the security game stimuli - 
namely manupulating base probability of theft and security price
"""


class Constants(BaseConstants):
    name_in_url = 'security_game_pretest'
    players_per_group = None
    security_efficacy = .01
    security_price_04 = .04
    base_theft_success_50 = .5
    endowment = 2
    security_price_02 = .02
    base_theft_success_75 = .75
    failed_attack = 1
    base_theft_success_60 = .6
    lost_from_attacks = 1
    tasks = ['PreTest50_04', 'PreTest50_02', 'PreTest60_04', 'PreTest60_02', 'PreTest75_04', 'PreTest75_02']
    num_rounds = len(tasks)


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, Constants.num_rounds+1))
            random.shuffle(round_numbers)
            p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))
            # print('p.participant.vars["task_rounds"] is:', p.participant.vars['task_rounds'])
            p.participant.vars['rounds_task'] = dict(zip(round_numbers, Constants.tasks))
    for p in subsession.get_players():
        p.page_in_round = str(p.participant.vars['rounds_task'][subsession.round_number])
pass


class Player(BasePlayer):
    security_consumed = models.CurrencyField(label="How much security would you like to purchase?", min=0)
    page_in_round = models.StringField()

    pass


class Group(BaseGroup):
    pass


# PAGES
class PreTest50_04(Page):
    form_model = 'player'
    form_fields = ['security_consumed']     # allows for security responses in page to ber recorded


    def is_displayed(self):         # this function passes the randomly-generated number for page-number pairing
        return self.round_number == self.participant.vars['task_rounds']['PreTest50_04']


    @staticmethod               # this function passes constants to javascript for manipulation in-page
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
    form_fields = ['security_consumed']


    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['PreTest50_02']

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


class PreTest60_02(Page):
    form_model = 'player'
    form_fields = ['security_consumed']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['PreTest60_02']


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



class PreTest60_04(Page):
    form_model = 'player'
    form_fields = ['security_consumed']


    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['PreTest60_04']


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


class PreTest75_02(Page):
    form_model = 'player'
    form_fields = ['security_consumed']


    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['PreTest75_02']


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


class PreTest75_04(Page):
    form_model = 'player'
    form_fields = ['security_consumed']


    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['PreTest75_04']


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



page_sequence = [PreTest50_04, PreTest50_02, PreTest60_04, PreTest60_02, PreTest75_04, PreTest75_02]
