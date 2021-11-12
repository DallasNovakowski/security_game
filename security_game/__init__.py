from otree.api import *

c = Currency

doc = """
The security game
"""

class Constants(BaseConstants):
    name_in_url = 'game'

    players_per_group = None
    num_rounds = 1
    security_price = .04
    security_efficacy = .01
    security_price_04 = .04
    base_theft_success_50 = .5
    security_price_02 = .02
    base_theft_success_75 = .75
    base_theft_success_60 = .6
    pass

class Subsession(BaseSubsession):
    pass

def creating_session(subsession):
    session = subsession.session
    session.endowment = session.config['endowment']
    session.lost_from_attacks = session.config['lost_from_attacks']
    session.failed_attack = session.config['failed_attack']
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
    # game
    security_consumed = models.CurrencyField(label="How much security would you like to purchase?", min=0)

    # pre game
    pre_partner_know = make_likert("I know whether my partner will try stealing from me")

    pre_partner_attempt = make_likert("My partner is probably going to try stealing from me")
    pre_success_prob = make_likert("If my partner tries to steal from me, they'll probably succeed")

    fair_game = make_likert("This game is fair")
    fair_distribution = make_likert("The way incomes were given for this game is fair")
    deserved_income = make_likert("I deserve my income for this game")
    deserved_role = make_likert("I deserve my role for this game")

    partner_fair = make_likert("My partner probably thinks this game is fair")
    partner_envy = make_likert("My partner probably feels envious of me")
    partner_jealous = make_likert("My partner probably feels jealous")
    partner_admiration = make_likert("My partner probably admires me")
    partner_frustrated = make_likert("My partner probably feels frustrated")

    # post game
    post_partner_attempt = make_likert("My partner is probably going to try stealing from me")
    post_success_prob = make_likert("If my partner tries to steal from me, they'll probably succeed")
    pass


# Pages
class Security_game(Page):
    form_model = 'player'
    form_fields = ['security_consumed']     # allows for security responses in page to ber recorded

    @staticmethod               # this function passes constants to javascript for manipulation in-page
    def js_vars(player):
        return dict(
            efficacy=Constants.security_efficacy,
            endowment= player.subsession.session.config['endowment'],
            price=Constants.security_price_04,
            theft_success=Constants.base_theft_success_50,
            lost_from_attacks=player.subsession.session.config['lost_from_attacks'],
            failed_attack=player.subsession.session.config['failed_attack'],
        )
    pass

class GameQs(Page):
    form_model = 'player'
    form_fields = ['security_consumed']     # allows for security responses in page to ber recorded


    pass


page_sequence = [Security_game]