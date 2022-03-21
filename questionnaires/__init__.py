from otree.api import *
c = Currency  # old name for currency; you can delete this.


class C(BaseConstants):
    NAME_IN_URL = 'security_questionnaires'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOWMENT = 2



def make_iu(label):
    return models.IntegerField(
        choices=[[1,"Not at all characteristic of me"],[2, "A little characteristic of me"],
                 [3, "Somewhat characteristic of me"],[4, "Very characteristic of me"],
                 [5, "Entirely characteristic of me"]],
        label=label,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )

def make_dospert(label):
    return models.IntegerField(
        choices=[[1,"Extremely Unlikely"],[2, "2"],
                 [3, "3"],[4, "4"],
                 [5, "5"], [6, "6"], [7, "Extremely Likely"]],
        label=label,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    submit_missing = models.IntegerField(initial=0)
    iu_1 = make_iu("Unforeseen events upset me greatly")
    iu_2 = make_iu("It frustrates me not having all the information I need.")
    iu_3 = make_iu("Uncertainty keeps me from living a full life.")
    iu_4 = make_iu("One should always look ahead so as to avoid surprises.")
    iu_5 = make_iu("A small unforeseen event can spoil everything, even with the best of planning.")
    iu_6 = make_iu("When it’s time to act, uncertainty paralyses me.")
    iu_7 = make_iu("When I am uncertain I can’t function very well.")
    iu_8 = make_iu("I always want to know what the future has in store for me.")
    iu_9 = make_iu("I can’t stand being taken by surprise.")
    iu_10 = make_iu("The smallest doubt can stop me from acting.")
    iu_11 = make_iu("I should be able to organize everything in advance.")
    iu_12 = make_iu("I must get away from all uncertain situations.")

    dospert_1 = make_dospert("Admitting that your tastes are different from those of a friend. ")
    dospert_2 = make_dospert("Going camping in the wilderness.")
    dospert_3 = make_dospert("Betting a day’s income at the horse races.")
    dospert_4 = make_dospert("Investing 10% of your annual income in a moderate growth mutual fund.")
    dospert_5 = make_dospert("Drinking heavily at a social function.")
    dospert_6 = make_dospert("Taking some questionable deductions on your income tax return.")
    dospert_7 = make_dospert("Disagreeing with an authority figure on a major issue.")
    dospert_8 = make_dospert("Betting a day’s income at a high-stake poker game.")
    dospert_9 = make_dospert("Having an affair with a married man/woman.")
    dospert_10 = make_dospert("Passing off somebody else’s work as your own. ")
    dospert_11 = make_dospert("Going down a ski run that is beyond your ability.")
    dospert_12 = make_dospert("Investing 5% of your annual income in a very speculative stock.")
    dospert_13 = make_dospert("Going whitewater rafting at high water in the spring.")
    dospert_14 = make_dospert("Betting a day’s income on the outcome of a sporting event")
    dospert_15 = make_dospert("Engaging in unprotected sex.")
    dospert_16 = make_dospert("Revealing a friend’s secret to someone else.")
    dospert_17 = make_dospert("Driving a car without wearing a seat belt.")
    dospert_18 = make_dospert("Investing 10% of your annual income in a new business venture.")
    dospert_19 = make_dospert("Taking a skydiving class.")
    dospert_20 = make_dospert("Riding a motorcycle without a helmet.")
    dospert_21 = make_dospert("Choosing a career that you truly enjoy over a more secure one.")
    dospert_22 = make_dospert("Speaking your mind about an unpopular issue in a meeting at work.")
    dospert_23 = make_dospert("Sunbathing without sunscreen.")
    dospert_24 = make_dospert("Bungee jumping off a tall bridge.")
    dospert_25 = make_dospert("Piloting a small plane.")
    dospert_26 = make_dospert("Walking home alone at night in an unsafe area of town.")
    dospert_27 = make_dospert("Moving to a city far away from your extended family.")
    dospert_28 = make_dospert("Starting a new career in your mid-thirties.")
    dospert_29 = make_dospert("Leaving your young children alone at home while running an errand.")
    dospert_30 = make_dospert("Not returning a wallet you found that contains $200.")
    pass


# PAGES
class IU(Page):
    form_model = 'player'
    form_fields = ['iu_1', 'iu_2', 'iu_3', 'iu_4', 'iu_5', 'iu_6', 'iu_7', 'iu_8', 'iu_9', 'iu_10', 'iu_11', 'iu_12']

    @staticmethod
    def error_message(player: Player, values):
        errors = {f: 'Please fill in this field' for f in values if not values[f]}
        if errors:
            player.submit_missing += 1
            if player.submit_missing < 2:
                return errors

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.submit_missing = 0

    pass
# any(len(ele) == 0 for ele in values):

class DOSPERT(Page):
    form_model = 'player'
    form_fields = ['dospert_1', 'dospert_2', 'dospert_3', 'dospert_4', 'dospert_5',
                   'dospert_6','dospert_7', 'dospert_8', 'dospert_9', 'dospert_10','dospert_11',
                   'dospert_12', 'dospert_13','dospert_14','dospert_15','dospert_16',
                   'dospert_17','dospert_18','dospert_19','dospert_20','dospert_21',
                   'dospert_22','dospert_23','dospert_24','dospert_25','dospert_26',
                   'dospert_27','dospert_28','dospert_29','dospert_30']

    @staticmethod
    def error_message(player: Player, values):
        errors = {f: 'Please fill in this field' for f in values if not values[f]}
        if errors:
            player.submit_missing += 1
            if player.submit_missing < 2:
                return errors

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.submit_missing = 0
    pass


page_sequence = [IU,DOSPERT]
