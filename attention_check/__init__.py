from otree.api import *


doc = """
This application provides an attention check
"""


class Constants(BaseConstants):
    name_in_url = 'attention_check'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    atn_check = models.StringField(label="", choices=[['Watching Athletics', 'Watching Athletics'], ['Attending Cultural Events', 'Attending Cultural Events'],
                                                      ['Participating in Athletics', 'Participating in Athletics'], ['Reading Outside of Work or School', 'Reading Outside of Work or School'],
                                                      ['Watching Movies', 'Watching Movies'], ['Travel', 'Travel'], ['Religious Activities', 'Religious Activities'],
                                                      ['Needlework', 'Needlework'], ['Cooking', 'Cooking'], ['Gardening', 'Gardening'], ['Computer Games', 'Computer Games'],
                                                      ['Hiking', 'Hiking'], ['Board or Card Games', 'Board or Card Games'], ['Other:', 'Other:']],
                                   widget=widgets.RadioSelect)
    other = models.StringField(label="", blank = True)
    ts_atncheck = models.FloatField(blank=True)
    # pass

class attention_check(Page):
    form_model = 'player'
    form_fields = ['atn_check', 'other', 'ts_atncheck']
    pass


page_sequence = [attention_check]


