from otree.api import *
from os import popen
c = Currency  # old name for currency; you can delete this.


class Constants(BaseConstants):
    name_in_url = 'consent'
    players_per_group = None
    num_rounds = 1


def creating_session(self):
    for p in self.get_players():
        otree_version = popen('otree --version').read().strip()
        print('built under otree version:', otree_version)
        p.otree_version = otree_version
pass


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    otree_version = models.StringField()
    consent = models.BooleanField(
    choices=[
        [False, 'No, I do not consent to participating in this study'],
        [True, 'Yes, I do consent to participating in this study'],
    ],
    label = 'Please indicate whether you consent to participating in this study:'
)

# FUNCTIONS
# PAGES
class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    # Control whether consent page is displayed based on name in config
    def is_displayed(player: Player):
        session = player.subsession.session
        return session.config['name'] == "security_game_pretest"

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        if not player.consent:
            return upcoming_apps[-1]


class ExpConsent(Page):
    form_model = 'player'
    form_fields =['consent']


# Control whether consent page is displayed based on name in config
    def is_displayed(player : Player):
        session = player.subsession.session
        return session.config['name'] == "security_game_merit" or session.config['name'] == "inequality_visibility_security" or \
               session.config['name'] == 'security_game_group'
pass

page_sequence = [Consent, ExpConsent]
