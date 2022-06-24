from otree.api import *
from os import popen
c = Currency  # old name for currency; you can delete this.


class C(BaseConstants):
    NAME_IN_URL = 'consent'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


def creating_session(self):
    for p in self.get_players():
        otree_version = popen('otree --version').read().strip()
        # print('built under otree version:', otree_version)
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
    atn_boost = models.IntegerField(
        choices=[[1,"Extremely Unlikely"],[2, "2"],
                 [3, "3"],[4, "4"],
                 [5, "5"], [6, "6"], [7, "Extremely Likely"]],
        label='Please indicate your likelihood of paying full attention during this study:',
        widget=widgets.RadioSelect
    )


# PAGES
# consent page for pretests
class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']

    # Control whether consent page is displayed based on name in config
    def is_displayed(player: Player):
        session = player.subsession.session
        return session.config['name'] == "security_game_pretest"

    @staticmethod       # populates a participant variable with the respondent's consent status (for use across apps)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.consent = player.consent

    @staticmethod       # sends nonconsenting participants to the last app
    def app_after_this_page(player, upcoming_apps):
        if not player.consent:
            return upcoming_apps[-1]

# consent page for hypothetical scenarios
class ExCo(Page):
    form_model = 'player'
    form_fields =['consent']
    template_name = 'consent/ExpConsent.html'

    # Control whether consent page is displayed based on name in config
    def is_displayed(player: Player):
        session = player.subsession.session
        return session.config['name'] == "security_game_merit" or session.config[
            'name'] == "inequality_visibility_security" or \
               session.config['name'] == 'security_game_group' or \
               session.config['name'] == 'ineq_sec'or \
               session.config['name'] == 'ineq_vis_expens' or \
               session.config['name'] == 'ineq_sec_stake' or \
               session.config['name'] == 'ineq_sec_uncertain' or \
               session.config['name'] == 'w_ineq_sec_uncertain'

    @staticmethod       # populates a participant variable with the respondent's consent status (for use across apps)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.consent = player.consent

    @staticmethod       # sends nonconsenting participants to the last app
    def app_after_this_page(player, upcoming_apps):
        if not player.consent:
            return upcoming_apps[-1]

#consent page for real payments
class ReCo(Page):
    form_model = 'player'
    form_fields =['consent']
    template_name = 'consent/RealConsent.html'

    # Control whether consent page is displayed based on name in config
    def is_displayed(player: Player):
        session = player.subsession.session
        return session.config['name'] == 'ineq_real' or session.config['name'] == 'ineq_sec_real'

    @staticmethod       # populates a participant variable with the respondent's consent status (for use across apps)
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.consent = player.consent

    @staticmethod       # sends nonconsenting participants to the last app
    def app_after_this_page(player, upcoming_apps):
        if not player.consent:
            return upcoming_apps[-1]

pass


class AtBo(Page):
    form_model = 'player'
    form_fields = ['atn_boost']
    template_name = 'consent/AttentionBoost.html'


page_sequence = [Consent, ExCo, ReCo, AtBo]
