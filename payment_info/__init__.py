import random
from otree.api import *


c = Currency  # old name for currency; you can delete this.


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1
    completion_codes = ['5sbhyjd', 'fvb^GWEV^', 'BFD%%$y','SDvnklk_','SdfNNMM<<%', 'sdfHHSeC', 'asdfea.>>>','doug_rides_bulls', '4dfsg##d']


class Subsession(BaseSubsession):
    def my_function(self):
        return "".join(random.choices(Constants.completion_codes, k =10))
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
        return session.config['name'] == "security_game_merit" or session.config['name'] == "inequality_visibility_security" or \
               session.config['name'] == 'security_game_group'
pass



page_sequence = [Security_Debrief]
