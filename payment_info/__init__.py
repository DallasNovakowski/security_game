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
    comments = models.LongStringField(label="Please leave any of your comments about this study here", blank=True)
    completion_code = models.StringField()
    pass


# FUNCTIONS
def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        player.completion_code = subsession.my_function()
        player.participant.vars['generated_code'] = player.completion_code


# PAGES
class PaymentInfo(Page):
    form_model = 'player'
    form_fields = ['completion_code']

class Study_end(Page)
    form_model = 'player'

    form_fields = ['comments']

page_sequence = [PaymentInfo, Study_end]
