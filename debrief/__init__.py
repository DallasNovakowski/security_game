import random
from otree.api import *


c = Currency  # old name for currency; you can delete this.


doc = """
This application is the dbrief - giving participants the option to re-consent, and describing the nature of the deception used
"""


class C(BaseConstants):
    NAME_IN_URL = 'debrief'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    COMPLETION_CODES = ['5sbhyjd', 'fvb^GWEV^', 'BFD%%$y','SDvnklk_','SdfNNMM<<%', 'sdfHHSeC', 'asdfea.>>>','doug_rides_bulls', '4dfsg##d']


class Subsession(BaseSubsession):
    def my_function(self):
        return "".join(random.choices(C.COMPLETION_CODES, k =10))
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    completion_code = models.StringField()
    reconsent = models.BooleanField(
        choices=[
            [True, 'Yes, I re-consent to my data being used in this study'],
            [False, 'No, I wish to withdraw my data from this study'],
        ],
        label='Given the use of deception in this study, you may have changed your willingness to participate in this study. '
              'Please indicate whether you consent to your data being used in this study, or you would prefer to withdraw your data (which will not affect your compensation).'
    )
    pass


# FUNCTIONS
def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        player.completion_code = subsession.my_function()
        player.participant.vars['generated_code'] = player.completion_code


# PAGES


class Security_Debrief(Page):
    form_model = 'player'
    form_fields = ['reconsent']
    def is_displayed(player : Player):
        session = player.subsession.session
        return session.config['name'] == 'ineq_sec_real' or session.config['name'] == 'ineq_sec_real_prime'
pass

page_sequence = [Security_Debrief]
