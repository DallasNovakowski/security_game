import random
from otree.api import *


# c = Currency  # old name for currency; you can delete this.


doc = """
This application is the dbrief - giving participants the option to re-consent, and describing the nature of the deception used
"""


class C(BaseConstants):
    NAME_IN_URL = 'debrief'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    COMPLETION_CODES = ['5sbhyjd', 'fvb^GWEV^', 'BFD%%$y','SDvnklk_','SdfNNMM<<%', 'sdfHHSeC', 'asdfea.>>>','doug_rides_bulls', '4dfsg##d']
    SECURITY_EFFICACY = .005
    BASE_THEFT_SUCCESS_50 = .5
    # base_theft_success_75 = .75
    # base_theft_success_60 = .6
    pass

class Subsession(BaseSubsession):
    def my_function(self):
        return "".join(random.choices(C.COMPLETION_CODES, k =10))
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    completion_code = models.StringField()
    reconsent = models.BooleanField(
        choices=[
            [True, 'Yes, I re-consent to my data being used in this study'],
            [False, 'No, I wish to withdraw my data from this study'],
        ],
        label='Now that you have full knowledge, please indicate whether you consent to your data being used in this study, or you would prefer to withdraw your data (which will not affect your base compensation, but disqualify you from the bonus payment).'
    )
    pass


# FUNCTIONS
def creating_session(subsession: Subsession):
    for player in subsession.get_players():
        player.completion_code = subsession.my_function()
        player.participant.vars['generated_code'] = player.completion_code
        # player.payoff_consumed = player.participant.payoff_consumed


# consumed {{ participant.payoff_consumed }}

# final payoff {{ participant.f_poff }}

# success {{ participant.success_theft }}



# PAGES
class PayoffDescription(Page):
    form_model = 'player'
    # form_fields = "final_payoff"

    @staticmethod               # this function passes constants to javascript for manipulation in-page
    def js_vars(player):
        return dict(
            efficacy= C.SECURITY_EFFICACY,
            endowment= player.subsession.session.config['p_endowment'],
            price=player.subsession.session.config["security_price"],
            theft_success= C.BASE_THEFT_SUCCESS_50,
            lost_from_attacks=player.subsession.session.config['p_lost_from_attacks'],
            failed_attack=player.subsession.session.config['p_failed_attack'],
            consumed= player.participant.vars['payoff_consumed'],
            final_payoff = player.participant.vars['f_poff'],
            success_theft = player.participant.vars["success_theft"]
        )

    # @staticmethod       # populates a participant variable with the respondent's consent status (for use across apps)
    # def before_next_page(player: Player, timeout_happened):
    #     print("the new theft success is", player.participant.vars['success_theft'])


    def is_displayed(player : Player):
        session = player.subsession.session
        return session.config['name'] == 'ineq_sec_real' or session.config['name'] == 'ineq_sec_real_prime'

    pass



class Security_Debrief(Page):
    form_model = 'player'
    form_fields = ['reconsent']
    def is_displayed(player : Player):
        session = player.subsession.session
        return session.config['name'] == 'ineq_sec_real' or session.config['name'] == 'ineq_sec_real_prime'
pass

page_sequence = [PayoffDescription, Security_Debrief]
