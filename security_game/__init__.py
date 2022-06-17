from otree.api import *

c = Currency

doc = """
The security game
"""

class C(BaseConstants):
    NAME_IN_URL = 'game'

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
    security_consumed = models.CurrencyField(label="How much security would you like to purchase?", min=0)
    security_desired = models.BooleanField(label='Would you like to purchase any units of security?')


    #     models.StringField(
    #     choices=[['yes', 'yes'], ['no', 'no']],
    #     label='Would you like to purchase any security?',
    #     widget=widgets.RadioSelect,
    #  blank = True
    # )
    # pre game
    pre_partner_attempt = make_likert("My partner is probably going to try stealing from me")
    # pre_success_prob = make_likert("If my partner tries to steal from me, they'll probably succeed")
    # pre_partner_know = make_likert("I know whether my partner will try stealing from me")
    # fair_game = make_likert("This game is fair")

    partner_reasonable_income = make_likert("My partner's assigned income is fair")
    reasonable_income = make_likert("My assigned income is fair")
    fair_distribution = make_likert("The way incomes were given for this game is fair")

    # earned_income = make_likert("I believe I have earned my income")
    # deserved_income = make_likert("I deserve my income for this game")
    # deserved_role = make_likert("I deserve my role for this game")
    # partner_deserved_income = make_likert("My partner's income is deserved")
    # partner_earned_income = make_likert("I believe my partner has earned their income")
    # guilty = make_likert("I feel guilty for my position in this game")
    # want_money = make_likert("In this game, I want to try to keep as much of my money as possible")

    # p_partner_fair = make_likert("My partner probably thinks this game is fair")
    # partner_admiration = make_likert("My partner probably admires me")

    p_partner_envy = make_likert("My partner probably feels envious of me")
    p_partner_jealous = make_likert("My partner probably feels jealous of me")
    p_partner_bitter = make_likert("My partner probably feels bitter")

    # post game

    # post_partner_attempt = make_likert("My partner is probably going to try stealing from me")
    # post_success_prob = make_likert("If my partner tries to steal from me, they'll probably succeed")
    pass


# Pages
class SecurityDesire(Page):
    form_model = 'player'
    form_fields = ['security_desired']     # allows for security responses in page to ber recorded

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
    pass

class GameQs(Page):
    form_model = 'player'
    form_fields = ['pre_partner_attempt','p_partner_envy','p_partner_jealous', 'p_partner_bitter', 'partner_reasonable_income',
    'reasonable_income','fair_distribution']

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


page_sequence = [SecurityDesire,GameQs, Security_game]