from otree.api import *


# This function assigns participants to treatment
# def creating_session(subsession):
#     import random
#     for player in subsession.get_players():
#         player.outgroup = random.choice([True, False])
#         player.agentic = random.choice([True, False])
#         print('set outgroup to', player.outgroup, 'and agentic to', player.agentic)


class C(BaseConstants):
    NAME_IN_URL = 'mg'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    OTHER_END = 150


class Player(BasePlayer):
    # Utility variables
    prolific_id = models.StringField(default=str(""))

    # Study variables
    num_dots = models.IntegerField(label='How many dots were in the image?', min=1, max=100)
    # agentic = models.BooleanField(blank=True)
    # outgroup = models.BooleanField(blank=True)
    pass


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# PAGES
class GroupWait(Page):
    form_model = 'player'
    timeout_seconds = 5
    pass

class PartnerWait(Page):
    form_model = 'player'
    timeout_seconds = 5
    pass

class ImageDesc(Page):
    form_model = 'player'
    template_name = 'min_group/stim_desc.html'
    pass


class Dots(Page):
    form_model = 'player'
    timeout_seconds = 3
    template_name = 'group_manip/group_stim.html'
    pass


class NumDots(Page):
    form_model = 'player'
    form_fields = ['num_dots']
    pass


class TaskIntro(Page):
    form_model = 'player'



# conditional pages by treatment
class OA(Page):
    form_model = 'player'
    template_name = 'group_manip/outgroup_agent.html'

    def is_displayed(self):
        return self.outgroup == True and self.agentic == True
    pass


class OR(Page):
    form_model = 'player'
    template_name = 'group_manip/outgroup_random.html'


    def is_displayed(self):
        return self.outgroup == True and self.agentic == False
    pass


class IA(Page):
    form_model = 'player'
    template_name = 'group_manip/ingroup_agent.html'


    def is_displayed(self):
        return self.outgroup == False and self.agentic == True
    pass


class IR(Page):
    form_model = 'player'
    template_name = 'group_manip/ingroup_random.html'


    def is_displayed(self):
        return self.outgroup == False and self.agentic == False
    pass


class security_intro(Page):
    form_model = 'player'
    pass


page_sequence = [
    # GroupWait,
    ImageDesc, Dots, NumDots,
    # PartnerWait,
    TaskIntro
    # , OA, OR,
    #              IA, IR, security_intro
]
