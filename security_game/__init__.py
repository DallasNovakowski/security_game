from otree.api import *

c = Currency

doc = """
This app is a basic sample of the security game
"""


class Constants(BaseConstants):
    name_in_url = 'security_game'
    players_per_group = None
    num_rounds = 1
    security_price = .04
    security_efficacy = .01
    security_price_04 = .04
    base_theft_success_50 = .5
    endowment = 2
    other_end = 1
    security_price_02 = .02
    base_theft_success_75 = .75
    failed_attack = 1
    base_theft_success_60 = .6
    lost_from_attacks = 1


class Subsession(BaseSubsession):
    pass


# This function assigns participants to treatment
def creating_session(subsession):
    import random
    for player in subsession.get_players():
        player.inequality = random.choice([True, False])
        player.visible = random.choice([True, False])
        print('set inequality to', player.inequality, 'and visibility to', player.visible)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Utility variables
    prolific_id = models.StringField(default=str(""))
    ts_preamble = models.FloatField(blank=True)
    ts_intro = models.FloatField(blank=True)
    ts_security = models.FloatField(blank=True)
    # Study variables
    visible = models.BooleanField(blank=True)
    inequality = models.BooleanField(blank=True)
    security_consumed = models.CurrencyField(label="How much security would you like to purchase?", min=0)
    pass


# PAGES
class Task_intro(Page):
    form_model = 'player'
    form_fields = ['ts_preamble']

    @staticmethod
    def before_next_page(self, timeout_happened):
        self.prolific_id = self.participant.label
    pass


class Equal_visible(Page):
    form_model = 'player'
    form_fields = ['ts_intro']

    def is_displayed(self):         # this function passes the randomly-generated number for page-number pairing
        return self.inequality == False and self.visible == True


class Equal_invisible(Page):
    form_model = 'player'
    form_fields = ['ts_intro']

    def is_displayed(self):
        return self.inequality == False and self.visible == False


class Unequal_invisible(Page):
    form_model = 'player'
    form_fields = ['ts_intro']

    def is_displayed(self):
        return self.inequality == True and self.visible == False


class Unequal_visible(Page):
    form_model = 'player'
    form_fields = ['ts_intro']

    def is_displayed(self):
        return self.inequality == True and self.visible == True


class Security_game(Page):
    form_model = 'player'
    form_fields = ['security_consumed', 'ts_security']     # allows for security responses in page to ber recorded

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


page_sequence = [Task_intro, Equal_visible, Equal_invisible, Unequal_visible, Unequal_invisible, Security_game]