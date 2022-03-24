from otree.api import *

import random

from otree.models import player

c = Currency

doc = """
This app is designed as a Sec_ of the security game stimuli - 
namely manupulating base probability of theft and security price
"""


class C(BaseConstants):
    NAME_IN_URL = 'security_game_Sec_'
    PLAYERS_PER_GROUP = None
    SECURITY_EFFICACY = .01
    BASE_THEFT_SUCCESS_50 = .5
    ENDOWMENT_2 = 2
    SECURITY_PRICE_02 = .02
    FAILED_ATTACK = 1
    BASE_THEFT_SUCCESS_60 = .6
    LOST_FROM_ATTACKS = 1
    TASKS = ['Sec_50_02', 'Sec_60_02', 'Sec_50_02_histak']
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
            p.inequality = random.choice([True, False])
            p.participant.vars['inequality'] = p.inequality
            # session = p.subsession.session
            print('set inequality to', p.inequality)
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
    inequality = models.BooleanField(blank=True)

    pre_partner_attempt = make_likert("My partner is probably going to try stealing from me")
    p_partner_envy = make_likert("My partner probably feels envious of me")
    p_partner_jealous = make_likert("My partner probably feels jealous of me")
    p_partner_frustrated = make_likert("My partner probably feels frustrated")
    p_partner_bitter = make_likert("My partner probably feels bitter")
    pass


class Group(BaseGroup):
    pass


# PAGES
class Task_intro(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == 1 and \
               self.participant.vars['session_name'] == 'ineq_sec_stake'


class Task_intro_r(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.round_number == 1 and \
               self.participant.vars['session_name'] == 'ineq_sec_real'

    # @staticmethod
    # def before_next_page(self, timeout_happened):
    #     self.prolific_id = self.participant.label
    # pass



class GroupWait(Page):
    form_model = 'player'
    timeout_seconds = 5

    def is_displayed(self):
        return self.round_number == 1 and \
               self.participant.vars['session_name'] == 'ineq_sec_real'
    pass

class scen_q(Page):
    form_model = 'player'
    form_fields = ['pre_partner_attempt','p_partner_envy','p_partner_jealous','p_partner_frustrated', 'p_partner_bitter']

    def is_displayed(self):
        return self.participant.vars['session_name'] == 'ineq_sec_stake' and \
               self.round_number == self.participant.vars['task_rounds']['Sec_50_02'] or \
               self.participant.vars['session_name'] == 'ineq_sec_stake' and \
               self.round_number == self.participant.vars['task_rounds']['Sec_50_02_histak']

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

class scen_q1(Page):
    template_name = 'security_game_mixed/scen_q.html'
    form_model = 'player'
    form_fields = ['pre_partner_attempt','p_partner_envy','p_partner_jealous','p_partner_frustrated', 'p_partner_bitter']

    def is_displayed(self):
        return self.participant.vars['session_name'] == 'ineq_sec_real' and \
               self.round_number == self.participant.vars['task_rounds']['Sec_50_02_histak'] or \
               self.participant.vars['session_name'] == 'ineq_sec_real' and \
               self.round_number == self.participant.vars['task_rounds']['Sec_60_02']

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

class UV(Page):
    form_model = 'player'
    template_name = 'security_game_mixed/Unequal_visible.html'

    def is_displayed(self):
        return self.participant.vars['inequality'] == True and \
               self.round_number == self.participant.vars['task_rounds']['Sec_50_02'] and \
               self.participant.vars['session_name'] == 'ineq_sec_stake'


class UVHS(Page):
    form_model = 'player'
    template_name = 'security_game_mixed/Unequal_visible_histak.html'

    def is_displayed(self):
        return self.participant.vars['inequality'] == True and \
               self.round_number == self.participant.vars['task_rounds']['Sec_50_02_histak'] or \
               self.participant.vars['inequality'] == True and \
               self.round_number == self.participant.vars['task_rounds']['Sec_60_02'] and \
               self.participant.vars['session_name'] == 'ineq_sec_real'

class EV(Page):
    form_model = 'player'
    template_name = 'security_game_mixed/Equal_visible.html'
    def is_displayed(self):
        return self.participant.vars['inequality'] == False and \
               self.round_number == self.participant.vars['task_rounds']['Sec_50_02'] and\
               self.participant.vars['session_name'] == 'ineq_sec_stake'


class EVHS(Page):
    form_model = 'player'
    template_name = 'security_game_mixed/Equal_visible_histak.html'
    def is_displayed(self):
        return self.participant.vars['inequality'] == False and \
               self.round_number == self.participant.vars['task_rounds']['Sec_50_02_histak'] or \
               self.participant.vars['inequality'] == False and \
               self.round_number == self.participant.vars['task_rounds']['Sec_60_02'] and \
               self.participant.vars['session_name'] == 'ineq_sec_real'


# and \
# self.participant.vars['session_name'] == 'ineq_sec_stake'

class Sec_50_02(Page):
    form_model = 'player'
    form_fields = ['security_consumed']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['Sec_50_02'] and \
               self.participant.vars['session_name'] == 'ineq_sec_stake'


    @staticmethod
    def js_vars(player):
        return dict(
            efficacy=C.SECURITY_EFFICACY,
            endowment=C.ENDOWMENT_2,
            price=C.SECURITY_PRICE_02,
            theft_success=C.BASE_THEFT_SUCCESS_50,
            lost_from_attacks=C.LOST_FROM_ATTACKS,
            failed_attack=C.FAILED_ATTACK,
        )
    pass


class Sec_60_02(Page):
    form_model = 'player'
    form_fields = ['security_consumed']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['Sec_60_02'] and \
               self.participant.vars['session_name'] == 'ineq_sec_real'

    @staticmethod
    def js_vars(player):
        return dict(
            efficacy=C.SECURITY_EFFICACY,
            endowment=C.ENDOWMENT_2*150,
            price=C.SECURITY_PRICE_02*150,
            theft_success=C.BASE_THEFT_SUCCESS_60,
            lost_from_attacks=C.LOST_FROM_ATTACKS*150,
            failed_attack=C.FAILED_ATTACK*150,
        )
    pass


class Sec_50_02_histak(Page):
    form_model = 'player'
    form_fields = ['security_consumed']

    def is_displayed(self):
        return self.round_number == self.participant.vars['task_rounds']['Sec_50_02_histak']


    @staticmethod
    def js_vars(player):
        return dict(
            efficacy=C.SECURITY_EFFICACY,
            endowment=C.ENDOWMENT_2*150,
            price=C.SECURITY_PRICE_02*150,
            theft_success=C.BASE_THEFT_SUCCESS_50,
            lost_from_attacks=C.LOST_FROM_ATTACKS*150,
            failed_attack=C.FAILED_ATTACK*150,
        )
    pass


page_sequence = [Task_intro, GroupWait, Task_intro_r,  EV, UV,  UVHS, EVHS, scen_q, scen_q1, Sec_50_02_histak, Sec_50_02, Sec_60_02]
