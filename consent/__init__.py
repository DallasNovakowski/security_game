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
        # p.participant.vars['otree_version'] = otree_version
        print('built under otree version:', otree_version)
        p.otree_version = otree_version
pass


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    otree_version = models.StringField()
    ts_consent = models.FloatField(blank=True)
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
    form_fields = ['consent', 'ts_consent']

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        if not player.consent:
            return upcoming_apps[-1]

page_sequence = [Consent]
