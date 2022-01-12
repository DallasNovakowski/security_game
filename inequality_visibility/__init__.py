from otree.api import *


# This function assigns participants to treatment
def creating_session(subsession):
    import random
    for player in subsession.get_players():
        session = player.subsession.session
        player.inequality = random.choice([True, False])
        if session.config['name'] != 'ineq_real' or session.config['name'] != 'ineq_sec':
            player.visible = random.choice([True, False])
        else: player.visible = random.choice([True])
        print('set inequality to', player.inequality, 'and visibility to', player.visible)



class Constants(BaseConstants):
    name_in_url = 'TI'
    players_per_group = None
    num_rounds = 1
    other_end = 1


class Player(BasePlayer):
    # Utility variables
    prolific_id = models.StringField(default=str(""))

    # Study variables
    visible = models.BooleanField(blank=True)
    inequality = models.BooleanField(blank=True)
    pass


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# PAGES
class Task_intro(Page):
    form_model = 'player'

    @staticmethod
    def before_next_page(self, timeout_happened):
        self.prolific_id = self.participant.label
    pass


class EV(Page):
    form_model = 'player'
    template_name = 'inequality_visibility/Equal_visible.html'
    def is_displayed(self):         # this function passes the randomly-generated number for page-number pairing
        return self.inequality == False and self.visible == True


class EI(Page):
    form_model = 'player'
    template_name = 'inequality_visibility/Equal_invisible.html'

    def is_displayed(self):
        return self.inequality == False and self.visible == False


class UI(Page):
    form_model = 'player'
    template_name = 'inequality_visibility/Unequal_invisible.html'

    def is_displayed(self):
        return self.inequality == True and self.visible == False


class UV(Page):
    form_model = 'player'
    template_name = 'inequality_visibility/Unequal_visible.html'

    def is_displayed(self):
        return self.inequality == True and self.visible == True


page_sequence = [Task_intro, EV, EI, UI, UV]
