from otree.api import *

import random

from otree.models import player

c = Currency

doc = """
This app is designed as a variant of the security game stimuli - 
namely manupulating base probability of theft stake sizes within subjects, along with a between-subjects manipulation of inequality
"""


class C(BaseConstants):
    NAME_IN_URL = 'security_game_Sec_w'
    PLAYERS_PER_GROUP = None
    SECURITY_EFFICACY = .003
    BASE_THEFT_SUCCESS = .2
    ENDOWMENT = 300
    SECURITY_PRICE = 2
    FAILED_ATTACK = 30
    LOST_FROM_ATTACKS = 150
    TASKS = ['Sec_20_ineq', 'Sec_20_eq']
    NUM_ROUNDS = len(TASKS)


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    import random
    if subsession.round_number == 1:
        for p in subsession.get_players():
            round_numbers = list(range(1, C.NUM_ROUNDS + 1))
            random.shuffle(round_numbers)
            p.participant.vars['task_rounds'] = dict(zip(C.TASKS, round_numbers))
            print('p.participant.vars["task_rounds"] is:', p.participant.vars['task_rounds'])
            p.participant.vars['rounds_task'] = dict(zip(round_numbers, C.TASKS))
            session = p.subsession.session
            p.participant.vars['session_name'] = p.session.config['name']
            # session = p.subsession.session
    for p in subsession.get_players():
        p.page_in_round = str(p.participant.vars['rounds_task'][subsession.round_number])

pass

def make_likert(label):
    return models.IntegerField(
        choices=[[1,"Strongly Disagree"],[2, "2"],
                 [3, "3"],[4, "4"],
                 [5, "5"], [6, "6"], [7, "Strongly Agree"]],
        label=label,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )


class Player(BasePlayer):
    submit_missing = models.IntegerField(initial=0)
    security_consumed = models.CurrencyField(label="How much security would you like to purchase?", min=0)
    page_in_round = models.StringField()
    # inequality = models.BooleanField(blank=True)

    p_inequality = make_likert("In this game, the money has been split unequally")
    pre_partner_attempt = make_likert("My partner is probably going to try stealing from me")
    p_partner_envy = make_likert("My partner probably feels envious of me")
    p_partner_jealous = make_likert("My partner probably feels jealous of me")
    p_partner_bitter = make_likert("My partner probably feels bitter")
    pass


class Group(BaseGroup):
    pass


# PAGES
class Task_intro(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == 1

class NextScen(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == 2



class scen_q(Page):
    form_model = 'player'
    form_fields = ['p_inequality', 'pre_partner_attempt', 'p_partner_envy', 'p_partner_jealous', 'p_partner_bitter']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['Sec_20_ineq'] or \
               self.round_number == self.participant.vars['task_rounds']['Sec_20_eq']

    @staticmethod
    def error_message(player: Player, values):
        errors = {f: 'Please fill in this field' for f in values if not values[f]}
        if errors:
            player.submit_missing += 1
            if player.submit_missing < 2:
                return errors

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.submit_missing = 0
    pass


class UVHS(Page):
    form_model = 'player'
    template_name = 'security_game_w_ineq/Unequal_visible_histak.html'

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['Sec_20_ineq']


class EVHS(Page):
    form_model = 'player'
    template_name = 'security_game_w_ineq/Equal_visible_histak.html'
    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['Sec_20_eq']


class Sec_20_ineq(Page):
    form_model = 'player'
    template_name = 'security_game_w_ineq/Sec_20.html'
    form_fields = ['security_consumed']


    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['Sec_20_ineq']

    @staticmethod
    def js_vars(player):
        return dict(
            efficacy=C.SECURITY_EFFICACY,
            endowment=C.ENDOWMENT,
            price=C.SECURITY_PRICE,
            theft_success=C.BASE_THEFT_SUCCESS,
            lost_from_attacks=C.LOST_FROM_ATTACKS,
            failed_attack=C.FAILED_ATTACK,
        )
    pass


class Sec_20_eq(Page):
    form_model = 'player'
    template_name = 'security_game_w_ineq/Sec_20.html'
    form_fields = ['security_consumed']


    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['Sec_20_eq']

    @staticmethod
    def js_vars(player):
        return dict(
            efficacy=C.SECURITY_EFFICACY,
            endowment=C.ENDOWMENT,
            price=C.SECURITY_PRICE,
            theft_success=C.BASE_THEFT_SUCCESS,
            lost_from_attacks=C.LOST_FROM_ATTACKS,
            failed_attack=C.FAILED_ATTACK,
        )
    pass



page_sequence = [Task_intro, NextScen, UVHS, EVHS, scen_q, Sec_20_ineq, Sec_20_eq]
