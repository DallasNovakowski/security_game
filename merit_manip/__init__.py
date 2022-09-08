from otree.api import *


# This function assigns participants to treatment
# def creating_session(subsession):
    # import random
    # for player in subsession.get_players():
        # player.inequality = random.choice([True, False])
        # player.merit = random.choice([True, False])
        # print('set inequality to', player.inequality, 'and merit to', player.merit)
        # player.merit = player.participant.vars['merit']
        # print('repeated merit is', player.merit)


class C(BaseConstants):
    NAME_IN_URL = 'MTI'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    OTHER_END = 150


class Player(BasePlayer):
    # Study variables
    # merit = models.BooleanField(blank=True)
    # inequality = models.BooleanField(blank=True)
    pass


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# PAGES
class Task_intro(Page):
    form_model = 'player'



class EM(Page):
    form_model = 'player'
    template_name = 'merit_manip/Equal_merit.html'

    def is_displayed(self):
        return False
            # self.inequality == False and self.participant.vars['merit']==True


class ER(Page):
    form_model = 'player'
    template_name = 'merit_manip/Equal_random.html'

    def is_displayed(self):
        return self.participant.vars['inequality_merit'] == "equal_random"
        # return self.inequality == False and self.participant.vars['merit'] == False


class UR(Page):
    form_model = 'player'
    template_name = 'merit_manip/Unequal_random.html'

    def is_displayed(self):
        # return self.inequality == True and self.participant.vars['merit'] == False
        return self.participant.vars['inequality_merit'] == "unequal_random"


class UM(Page):
    form_model = 'player'
    template_name = 'merit_manip/Unequal_merit.html'

    def is_displayed(self):
        # return self.inequality == True and self.participant.vars['merit'] == True
        return self.participant.vars['inequality_merit'] == "unequal_merit"





class UuM(Page):
    form_model = 'player'
    template_name = 'merit_manip/Unequal_unmerit.html'

    def is_displayed(self):
        # return self.inequality == True and self.participant.vars['merit'] == True
        return self.participant.vars['inequality_merit'] == "unequal_unmerit"



class GameDesc(Page):
    form_model = 'player'


page_sequence = [
    # Task_intro,
    #              EM,
    ER, UM, UuM, UR
    # , GameDesc
]
