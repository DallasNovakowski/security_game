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
    security_price_02 = .02
    base_theft_success_75 = .75
    failed_attack = 1
    base_theft_success_60 = .6
    lost_from_attacks = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prolific_id = models.StringField(default=str(""))
    security_consumed = models.CurrencyField(label="How much security would you like to purchase?", min=0)
    ts_intro = models.FloatField(blank=True)
    ts_security = models.FloatField(blank=True)
    inequality = models.BooleanField()
    pass


    def creating_session(subsession):
        import random
        for player in subsession.get_players():
            player.inequality = random.choice([True, False])
            print('set inequality to', player.inequality)


# PAGES
class security_game(Page):
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


class Task_intro(Page):
    form_model = 'player'
    form_fields = ['ts_intro']

    @staticmethod
    def before_next_page(self, timeout_happened):
        self.prolific_id = self.participant.label
    pass

page_sequence = [Task_intro, security_game]