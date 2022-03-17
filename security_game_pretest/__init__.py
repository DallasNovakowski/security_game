from otree.api import *

import random

from otree.models import player

c = Currency

doc = """
This app is designed as a pretest of the security game stimuli - 
namely manupulating base probability of theft and security price
"""


class C(BaseConstants):
    NAME_IN_URL = 'security_game_pretest'
    PLAYERS_PER_GROUP = None
    SECURITY_EFFICACY = .01
    SECURITY_PRICE_04 = .04
    BASE_THEFT_SUCCESS_50 = .5
    ENDOWMENT = 2
    SECURITY_PRICE_02 = .02
    BASE_THEFT_SUCCESS_75 = .75
    FAILED_ATTACK = 1
    BASE_THEFT_SUCCESS_60 = .6
    LOST_FROM_ATTACKS = 1
    TASKS = ['PreTest50_04', 'PreTest50_02', 'PreTest60_04', 'PreTest60_02', 'PreTest75_04', 'PreTest75_02']
    NUM_ROUNDS = len(TASKS)


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, C.NUM_ROUNDS+1))
            random.shuffle(round_numbers)
            p.participant.vars['task_rounds'] = dict(zip(C.TASKS, round_numbers))
            # print('p.participant.vars["task_rounds"] is:', p.participant.vars['task_rounds'])
            p.participant.vars['rounds_task'] = dict(zip(round_numbers, C.TASKS))
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
            efficacy=C.SECURITY_EFFICACY,
            endowment=C.ENDOWMENT,
            price=C.SECURITY_PRICE_04,
            theft_success=C.BASE_THEFT_SUCCESS_50,
            lost_from_attacks=C.LOST_FROM_ATTACKS,
            failed_attack=C.FAILED_ATTACK,
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
            efficacy=C.SECURITY_EFFICACY,
            endowment=C.ENDOWMENT,
            price=C.SECURITY_PRICE_02,
            theft_success=C.BASE_THEFT_SUCCESS_50,
            lost_from_attacks=C.LOST_FROM_ATTACKS,
            failed_attack=C.FAILED_ATTACK,
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
            efficacy=C.SECURITY_EFFICACY,
            endowment=C.ENDOWMENT,
            price=C.SECURITY_PRICE_02,
            theft_success=C.BASE_THEFT_SUCCESS_60,
            lost_from_attacks=C.LOST_FROM_ATTACKS,
            failed_attack=C.FAILED_ATTACK,
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
            efficacy=C.SECURITY_EFFICACY,
            endowment=C.ENDOWMENT,
            price=C.SECURITY_PRICE_04,
            theft_success=C.BASE_THEFT_SUCCESS_60,
            lost_from_attacks=C.LOST_FROM_ATTACKS,
            failed_attack=C.FAILED_ATTACK,
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
            efficacy=C.SECURITY_EFFICACY,
            endowment=C.ENDOWMENT,
            price=C.SECURITY_PRICE_02,
            theft_success=C.BASE_THEFT_SUCCESS_75,
            lost_from_attacks=C.LOST_FROM_ATTACKS,
            failed_attack=C.FAILED_ATTACK,
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
            efficacy=C.SECURITY_EFFICACY,
            endowment=C.ENDOWMENT,
            price=C.SECURITY_PRICE_04,
            theft_success=C.BASE_THEFT_SUCCESS_75,
            lost_from_attacks=C.LOST_FROM_ATTACKS,
            failed_attack=C.FAILED_ATTACK,
        )
    pass



page_sequence = [PreTest50_04, PreTest50_02, PreTest60_04, PreTest60_02, PreTest75_04, PreTest75_02]
