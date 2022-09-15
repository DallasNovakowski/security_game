from otree.api import *

c = Currency

doc = """
The security game
"""

class C(BaseConstants):
    NAME_IN_URL = 'pri_intro'

    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    SECURITY_EFFICACY = .01
    BASE_THEFT_SUCCESS_50 = .5
    # base_theft_success_75 = .75
    # base_theft_success_60 = .6
    pass

class Subsession(BaseSubsession):
    pass

def creating_session(subsession):
    import random
    session = subsession.session
    session.endowment = session.config['endowment']
    session.lost_from_attacks = session.config['lost_from_attacks']
    session.failed_attack = session.config['failed_attack']
    session.security_price = session.config['security_price']
    print("endowment for session is", session.endowment, ", and lost_from_attacks is",
          session.config['lost_from_attacks'], ", and failed_attack is", session.config['failed_attack'])
    if session.config['name'] == 'security_game_total_loss':
        for player in subsession.get_players():
            player.total_loss = random.choice([True,False])
            player.participant.vars['total_loss'] = player.total_loss
    if session.config['name'] == 'security_game_vis':
        for player in subsession.get_players():
            player.visible = random.choice([True,False])
            player.participant.vars['visible'] = player.visible



class Group(BaseGroup):
    pass

class Player(BasePlayer):
    total_loss = models.BooleanField(blank=True)
    visible = models.BooleanField(Blank=True)
    pass


# Pages
class Pri_intro(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.subsession.session.config['name'] == 'ineq_sec_real_prime'


    @staticmethod               # this function passes constants to javascript for manipulation in-page
    def js_vars(player):
        return dict(
            efficacy= C.SECURITY_EFFICACY,
            endowment= player.subsession.session.config['endowment'],
            price=player.subsession.session.config["security_price"],
            theft_success= C.BASE_THEFT_SUCCESS_50,
            lost_from_attacks=player.subsession.session.config['lost_from_attacks'],
            failed_attack=player.subsession.session.config['failed_attack'],
        )
    pass


class Pri_intro_hyp(Page):
    form_model = 'player'

    def is_displayed(self):
        return (self.subsession.session.config['name'] != 'ineq_sec_real_prime' and
                self.subsession.session.config['name'] != 'security_game_total_loss') or \
               (self.subsession.session.config['name'] == 'security_game_total_loss' and \
                self.participant.vars['total_loss'] == False)

    @staticmethod               # this function passes constants to javascript for manipulation in-page
    def js_vars(player):
        return dict(
            efficacy= C.SECURITY_EFFICACY,
            endowment= player.subsession.session.config['endowment'],
            price=player.subsession.session.config["security_price"],
            theft_success= C.BASE_THEFT_SUCCESS_50,
            lost_from_attacks=player.subsession.session.config['lost_from_attacks'],
            failed_attack=player.subsession.session.config['failed_attack'],
        )
    pass


class Pri_intro_hyp_tot_los(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.subsession.session.config['name'] == 'security_game_total_loss' and self.participant.vars['total_loss'] == True


    @staticmethod               # this function passes constants to javascript for manipulation in-page
    def js_vars(player):
        return dict(
            efficacy= C.SECURITY_EFFICACY,
            endowment= player.subsession.session.config['endowment'],
            price=player.subsession.session.config["security_price"],
            theft_success= C.BASE_THEFT_SUCCESS_50,
            lost_from_attacks=player.subsession.session.config['lost_from_attacks'],
            failed_attack=player.subsession.session.config['failed_attack'],
        )
    pass


class ESS_inv(Page):
    template_name = 'priming_intro/Equalsmallerstak_inv.html'
    form_model = 'player'

    def is_displayed(self):
        return self.subsession.session.config['name'] == 'security_game_vis' and self.participant.vars['visible'] == False



class ESS(Page):
    template_name = 'priming_intro/Equalsmallerstak.html'
    form_model = 'player'

    def is_displayed(self):
        return (self.subsession.session.config['name'] != 'security_game_vis') or \
                       (self.subsession.session.config['name'] == 'security_game_vis' and \
                        self.participant.vars['visible'] == True)

page_sequence = [Pri_intro, Pri_intro_hyp, Pri_intro_hyp_tot_los, ESS,ESS_inv]