from otree.api import *


# This function assigns participants to treatment
def creating_session(subsession):
    import random
    for player in subsession.get_players():
        player.inequality = random.choice([True, False])


class C(BaseConstants):
    NAME_IN_URL = 'im2b'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    OTHER_END = 150


class Player(BasePlayer):
    # Utility variables
    # prolific_id = models.StringField(default=str(""))
    # Study variables
    inequality = models.BooleanField(blank=True)
    pass

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Task_intro(Page):
    form_model = 'player'

    def is_displayed(self):
        return False
            # self.subsession.session.config['name'] != 'ineq_sec_real_prime'


    @staticmethod
    def before_next_page(self, timeout_happened):
        self.prolific_id = self.participant.label
    pass

class ER(Page):
    form_model = 'player'
    template_name = 'ineq_manip_2b/Equal_random.html'

    def is_displayed(self):
        return (self.subsession.session.config['name'] == 'security_game_vis' and self.inequality == False and self.participant.vars['visible'] == True) or \
               (self.subsession.session.config['name'] != 'security_game_vis' and self.inequality == False)

class ERI(Page):
    form_model = 'player'
    template_name = 'ineq_manip_2b/Equal_random_invis.html'

    def is_displayed(self):
        return (self.subsession.session.config['name'] == 'security_game_vis' and self.inequality == False and self.participant.vars['visible'] == False)


class UR(Page):
    form_model = 'player'
    template_name = 'ineq_manip_2b/Unequal_random.html'

    def is_displayed(self):
        return (self.subsession.session.config['name'] == 'security_game_vis' and self.inequality == True and self.participant.vars['visible'] == True) or \
               (self.subsession.session.config['name'] != 'security_game_vis' and self.inequality == True)

class URI(Page):
    form_model = 'player'
    template_name = 'ineq_manip_2b/Unequal_random_invis.html'

    def is_displayed(self):
        return (self.subsession.session.config['name'] == 'security_game_vis' and self.inequality == True and self.participant.vars['visible'] == False)


class GameDesc(Page):
    form_model = 'player'

page_sequence = [Task_intro, ER, ERI, UR, URI]
