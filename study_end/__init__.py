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
    comments = models.LongStringField(label="Please leave any of your comments about this study here", blank=True)
    pass


class Comments(Page):
    form_model = 'player'
    form_fields = ['comments']
    pass


class PaymentInfo(Page):
    form_model = 'player'

    def is_displayed(player):
        participant = player.participant
        return participant.consent == True

    @staticmethod
    def js_vars(player):
        return dict(
            completionlink=player.subsession.session.config['completionlink']
        )
    pass



page_sequence = [Comments, PaymentInfo]