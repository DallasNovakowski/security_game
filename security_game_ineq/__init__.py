from otree.api import *
import random

c = Currency

doc = """
The security game
"""

class C(BaseConstants):
    NAME_IN_URL = 'game_i'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    SECURITY_EFFICACY = .005
    BASE_THEFT_SUCCESS_50 = .5
    # base_theft_success_75 = .75
    # base_theft_success_60 = .6
    pass

class Subsession(BaseSubsession):
    pass

def creating_session(subsession):
    session = subsession.session
    session.endowment = session.config['endowment']
    session.lost_from_attacks = session.config['lost_from_attacks']
    session.failed_attack = session.config['failed_attack']
    session.security_price = session.config['security_price']
    print("endowment for session is", session.endowment, ", and lost_from_attacks is",
          session.config['lost_from_attacks'], ", and failed_attack is", session.config['failed_attack'])

# session.params = {}

class Group(BaseGroup):
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
    # game
    # prolific_id = models.StringField(default=str(""))
    security_consumed = models.CurrencyField(label="How much security would you like to purchase?", min=0)
    p_inequality = make_likert("In this game, the money has been split unequally")

    pre_partner_attempt = make_likert("My partner is probably going to try stealing from me")

    # partner_reasonable_income = make_likert("My partner's assigned income is fair")
    # reasonable_income = make_likert("My assigned income is fair")
    # fair_distribution = make_likert("The way incomes were given for this game is fair")

    p_partner_envy = make_likert("My partner probably feels envious of me")
    p_partner_jealous = make_likert("My partner probably feels jealous of me")
    p_partner_bitter = make_likert("My partner probably feels bitter")
    payoff_consumed = models.IntegerField()
    f_poff = models.CurrencyField()
    success_theft = models.IntegerField()
    pass


# Pages
class SecurityDesire(Page):
    form_model = 'player'
    # form_fields = ['security_desired']     # allows for security responses in page to ber recorded

    # @staticmethod               # this function passes constants to javascript for manipulation in-page
    # def js_vars(player):
    #     return dict(
    #         efficacy= C.SECURITY_EFFICACY,
    #         endowment= player.subsession.session.config['endowment'],
    #         price=player.subsession.session.config["security_price"],
    #         theft_success= C.BASE_THEFT_SUCCESS_50,
    #         lost_from_attacks=player.subsession.session.config['lost_from_attacks'],
    #         failed_attack=player.subsession.session.config['failed_attack'],
    #     )
    pass


class Security_game(Page):
    form_model = 'player'
    form_fields = ['security_consumed']     # allows for security responses in page to ber recorded

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

    # @staticmethod
    # def before_next_page(self, timeout_happened):
    #     self.prolific_id = self.participant.label
    #     self.participant.vars['consumed'] = self.security_consumed
    #     print(self.participant.vars['consumed'])
    # pass


    @staticmethod       # populates a participant variable with the respondent's consent status (for use across apps)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant

        participant.vars['payoff_consumed'] = player.security_consumed
        print("the value we're trying to display is,", player.participant.vars['payoff_consumed'])

        player.success_theft = max(random.choices([0, 1], weights=(C.BASE_THEFT_SUCCESS_50*100+
                                           player.participant.vars['payoff_consumed']*C.SECURITY_EFFICACY*100,
                                        C.BASE_THEFT_SUCCESS_50*100 -
                                        player.participant.vars['payoff_consumed']*C.SECURITY_EFFICACY*100), k=1))


        # player.payoff_consumed = player.participant.vars['payoff_consumed']
        if player.success_theft == 1:
            player.f_poff = 300 - player.participant.vars['payoff_consumed'] * player.subsession.session.config[
                "security_price"] - 100
            player.participant.vars['f_poff'] =player.f_poff
            # participant.f_poff = player.f_poff
            player.participant.vars['success_theft'] = player.success_theft
        else:
            player.f_poff = 300 - player.participant.vars['payoff_consumed'] * player.subsession.session.config[
                "security_price"]
            player.participant.vars['f_poff'] = player.f_poff
            # participant.f_poff = player.f_poff
            player.participant.vars['success_theft'] = player.success_theft

        print("the theft success is", player.participant.vars['success_theft'])

    pass





class GameQs(Page):
    form_model = 'player'
    form_fields = ['p_inequality','pre_partner_attempt','p_partner_envy','p_partner_jealous', 'p_partner_bitter'
    #     , 'partner_reasonable_income',
    # 'reasonable_income','fair_distribution'
                   ]

    # @staticmethod
    # def js_vars(player):    # highlights variables/fields that do not need to be filled (but that we'll be displaying a one-time warning message if they're left blank)
    #     return dict(optional_fields = GameQs.form_fields
    #                 #,required_fields = GameQs.form_fields[0:2]
    #     )

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

    pass

class NextScen(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.subsession.session.config['name'] == 'ineq_sec_real_prime'



page_sequence = [GameQs, Security_game
    # , NextScen
                 ]