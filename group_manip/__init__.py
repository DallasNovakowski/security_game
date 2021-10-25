from otree.api import *


# This function assigns participants to treatment
def creating_session(subsession):
    import random
    for player in subsession.get_players():
        player.outgroup = random.choice([True, False])
        player.agentic = random.choice([True, False])
        print('set outgroup to', player.outgroup, 'and agentic to', player.agentic)


class Constants(BaseConstants):
    name_in_url = 'group_manip'
    players_per_group = None
    num_rounds = 1
    other_end = 1


class Player(BasePlayer):
    # Utility variables
    prolific_id = models.StringField(default=str(""))
    ts_desc = models.FloatField(blank=True)
    ts_img = models.FloatField(blank=True)
    ts_dots = models.FloatField(blank=True)
    ts_preamble = models.FloatField(blank=True)
    ts_intro = models.FloatField(blank=True)
    ts_secintro = models.FloatField(blank=True)

    # Study variables
    num_dots = models.IntegerField(label='How many dots were in the image?', min=5, max=100)
    agentic = models.BooleanField(blank=True)
    outgroup = models.BooleanField(blank=True)
    pass


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


# PAGES
class group_wait(Page):
    form_model = 'player'
    timeout_seconds = 5
    pass

class partner_wait(Page):
    form_model = 'player'
    timeout_seconds = 5
    pass

class stim_desc(Page):
    form_model = 'player'
    form_fields = ['ts_desc']
    pass


class group_stim(Page):
    form_model = 'player'
    form_fields = ['ts_img']
    timeout_seconds = 4
    pass


class num_dots(Page):
    form_model = 'player'
    form_fields = ['num_dots', 'ts_dots']
    pass


class Task_intro(Page):
    form_model = 'player'
    form_fields = ['ts_preamble']

    @staticmethod
    def before_next_page(self, timeout_happened):
        self.prolific_id = self.participant.label
    pass


# conditional pages by treatment
class outgroup_agent(Page):
    form_model = 'player'
    form_fields = ['ts_intro']


    def is_displayed(self):
        return self.outgroup == True and self.agentic == True
    pass


class outgroup_random(Page):
    form_model = 'player'
    form_fields = ['ts_intro']


    def is_displayed(self):
        return self.outgroup == True and self.agentic == False
    pass


class ingroup_agent(Page):
    form_model = 'player'
    form_fields = ['ts_intro']


    def is_displayed(self):
        return self.outgroup == False and self.agentic == True
    pass


class ingroup_random(Page):
    form_model = 'player'
    form_fields = ['ts_intro']


    def is_displayed(self):
        return self.outgroup == False and self.agentic == False
    pass


class security_intro(Page):
    form_model = 'player'
    form_fields = ['ts_secintro']
    pass


page_sequence = [group_wait, stim_desc, group_stim, num_dots, partner_wait, Task_intro, outgroup_agent, outgroup_random,
                 ingroup_agent, ingroup_random, security_intro]
