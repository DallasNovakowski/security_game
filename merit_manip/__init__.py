from otree.api import *


# This function assigns participants to treatment
def creating_session(subsession):
    import random
    for player in subsession.get_players():
        player.inequality = random.choice([True, False])
        player.merit = random.choice([True, False])
        print('set inequality to', player.inequality, 'and merit to', player.merit)


class Constants(BaseConstants):
    name_in_url = 'MTI'
    players_per_group = None
    num_rounds = 1
    other_end = 1


class Player(BasePlayer):
    # Utility variables
    prolific_id = models.StringField(default=str(""))
    # Study variables
    merit = models.BooleanField(blank=True)
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


class EM(Page):
    form_model = 'player'
    template_name = 'consent/Equal_merit.html'

    def is_displayed(self):         # this function passes the randomly-generated number for page-number pairing
        return self.inequality == False and self.merit == True


class ER(Page):
    form_model = 'player'
    template_name = 'consent/Equal_random.html'

    def is_displayed(self):
        return self.inequality == False and self.merit == False


class UM(Page):
    form_model = 'player'
    template_name = 'consent/Unequal_merit.html'

    def is_displayed(self):
        return self.inequality == True and self.merit == True


class UR(Page):
    form_model = 'player'
    template_name = 'consent/Unequal_random.html'

    def is_displayed(self):
        return self.inequality == True and self.merit == False


page_sequence = [Task_intro, EM, ER, UM, UR]
