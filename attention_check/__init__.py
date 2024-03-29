from otree.api import *


doc = """
This application provides an attention check
"""


class C(BaseConstants):
    NAME_IN_URL = 'ac'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


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
    atn_other = models.StringField(label="", blank=True)
    # atn_check2 = models.StringField(label="", choices=[['Walking down the street at night', 'Walking down the street at night'],
    #                                                   ['Buying or selling goods', 'Buying or selling goods'],
    #                                                    ['Talking with my family', 'Talking with my family'],
    #                                                    ['Talking with my friends', 'Talking with my friends'],
    #                                                    ['Meeting new people', 'Meeting new people'],
    #                                                    ['Travelling to new places', 'Travelling to new places'],
    #                                                    ['Talking with work colleagues', 'Talking with work colleagues'],
    #                                                    ['On public transportation', 'On public transportation'],
    #                                                   ['Other:', 'Other:']],
    #                                widget=widgets.RadioSelect)
    # atn_other2 = models.StringField(label="", blank=True)
    comp_check = models.StringField(label="What best describes your role in this study?",
                                    choices=[['Deciding whether to accept an offer', 'Deciding whether to accept an offer'],
                                             ['Placing a bid', 'Placing a bid'],
                                             ['Paying my partner a wage', 'Paying my partner a wage'],
                                             ['Deciding whether to purchase a security product', 'Deciding whether to purchase a security product'],
                                             ['Donating funds to a shared project', 'Donating funds to a shared project']],
                                   widget=widgets.RadioSelect)

    # if self.subsession.session.config['name'] == 'security_game_vis'

    vis_check = models.StringField(label="Was your partner aware of how much money you received?",
                                    choices=[
                                        ['Yes', 'Yes'],
                                        ['No', 'No'],
                                        ['No information was given','No information was given'],
                                        ['Unsure','Unsure']
                                             ],
                                   widget=widgets.RadioSelect)


    # pass

class ac1(Page):
    form_model = 'player'
    form_fields = ['atn_check', 'atn_other']
    template_name = 'attention_check/attention_check.html'
    pass


# class ac2(Page):
#     form_model = 'player'
#     form_fields = ['atn_check2', 'atn_other2']
#     template_name = 'attention_check/attention_check2.html'
#     pass


class cc(Page):
    form_model = 'player'
    form_fields = ['comp_check', 'vis_check']
    template_name = 'attention_check/comprehension_check.html'
    pass


page_sequence = [ac1, cc]


