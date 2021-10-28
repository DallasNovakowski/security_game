import random
from otree.api import *


c = Currency  # old name for currency; you can delete this.


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'study_end'
    players_per_group = None
    num_rounds = 1
    pass

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    pass


class Study_End(Page):
    form_model = 'player'
    pass

page_sequence = [Study_End]