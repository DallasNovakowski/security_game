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


class Player(BasePlayer):
    # Utility variables
    # Study variables
    security_consumed = models.CurrencyField(label="How much security would you like to purchase?", min=0)
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


page_sequence = [Security_game]