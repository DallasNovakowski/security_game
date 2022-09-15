# from django.contrib import messages
from os import environ
from os import popen



# 'intro',

SESSION_CONFIGS = [
    dict(
        name='security_game_pretest',
        app_sequence=['consent', 'intro', 'security_game_pretest', 'questionnaires', 'attention_check', 'study_end'],
        num_demo_participants=5,
        completionlink='https://app.prolific.co/submissions/complete?cc=blahblahblah',
        oTree_version_used=popen('otree --version').read().strip()
    ),
    dict(
        name='ineq_sec_stake',
        app_sequence=["consent", "survey", 'security_game_mixed', 'attention_check','study_end'],
        num_demo_participants=5,
        completionlink='https://app.prolific.co/submissions/complete?cc=blahblahblah',
        endowment=2,
        lost_from_attacks=1,
        failed_attack=1,
        security_price=.02,
        OTREE_REST_KEY="1234"
    ),
    # dict(
    #     name='ineq_sec_uncertain',
    #     app_sequence=["consent", "survey", "ineq_manip_2b", 'security_game', 'attention_check', 'study_end'],
    #     num_demo_participants=5,
    #     completionlink='https://app.prolific.co/submissions/complete?cc=blahblahblah',
    #     endowment=300,
    #     lost_from_attacks=150,
    #     failed_attack=150,
    #     security_price=2,
    #     OTREE_REST_KEY="1234"
    # ),
    dict(
        name='w_ineq_sec_uncertain',
        app_sequence=["consent", "survey", "security_game_w_ineq", 'attention_check', 'study_end'],
        num_demo_participants=5,
        completionlink='https://app.prolific.co/submissions/complete?cc=552ABCA3',
        endowment=300,
        lost_from_attacks=150,
        failed_attack=150,
        security_price=2,
        OTREE_REST_KEY="1234"
    ),
    dict(
        name='ineq_sec_real_prime',
        app_sequence=["consent", "survey", "priming_intro", 'security_game',
                      "ineq_manip_2b",'security_game_ineq',
                                                                             # 'security_game_w_ineq',
                      'attention_check', 'debrief', 'study_end'],
        num_demo_participants=5,
        completionlink='https://app.prolific.co/submissions/complete?cc=552ABCA3',
        p_endowment=250,
        endowment=300,
        lost_from_attacks=100,
        p_lost_from_attacks=50,
        failed_attack=100,
        p_failed_attack=50,
        security_price=2,
        p_security_price=2,
        OTREE_REST_KEY="1234"
    ),
    # dict(
    #     name="security_game_merit_old",
    #     display_name="meritocracy_manip_old",
    #     num_demo_participants=15,
    #     app_sequence=["consent","survey","slider_task", 'merit_manip', 'security_game', 'attention_check', 'study_end'],
    #     completionlink='https://app.prolific.co/submissions/complete?cc=blahblah',
    #     endowment=300,
    #     lost_from_attacks=1,
    #     failed_attack=1,
    #     security_price=.02
    # ),
    dict(
        name="security_game_merit",
        display_name="meritocracy_manip",
        num_demo_participants=15,
        app_sequence=["consent", "survey", "priming_intro", 'security_game', "slider_task",
                      'merit_manip', 'security_game_ineq', 'attention_check', 'study_end'],
        completionlink='https://app.prolific.co/submissions/complete?cc=CWD58TF0',
        p_endowment=250,
        endowment=300,
        lost_from_attacks=100,
        p_lost_from_attacks=50,
        failed_attack=100,
        p_failed_attack=50,
        security_price=2,
        p_security_price=2,
        OTREE_REST_KEY="1234"
    ),
    # dict(
    #     name="security_game_group",
    #     display_name="group_agent",
    #     num_demo_participants=15,
    #     app_sequence=["consent","survey", "group_manip", 'security_game', 'attention_check', 'study_end'],
    #     completionlink='https://app.prolific.co/submissions/complete?cc=blahblah',
    #     endowment=2,
    #     lost_from_attacks=1,
    #     failed_attack=1,
    #     security_price=.02
    # )
    dict(
        name="security_game_group",
        display_name="group_agent",
        num_demo_participants=15,
        app_sequence=["consent", "survey", "priming_intro", 'security_game', "min_group", "group_manip",
                      'security_game_ineq', 'attention_check', 'study_end'],
        completionlink='https://app.prolific.co/submissions/complete?cc=CWD58TF0',
        p_endowment=250,
        endowment=300,
        lost_from_attacks=100,
        p_lost_from_attacks=50,
        failed_attack=100,
        p_failed_attack=50,
        security_price=2,
        p_security_price=2,
        OTREE_REST_KEY="1234"
    ),

dict(
    name="security_game_unmerit",
    display_name="unmerit_manip",
    num_demo_participants=15,
    app_sequence=["consent", "survey", "priming_intro", 'security_game', "slider_task",
                  'merit_manip', 'security_game_ineq', 'attention_check', 'study_end'],
    completionlink='https://app.prolific.co/submissions/complete?cc=CWD58TF0',
    p_endowment=250,
    endowment=300,
    lost_from_attacks=100,
    p_lost_from_attacks=50,
    failed_attack=100,
    p_failed_attack=50,
    security_price=2,
    p_security_price=2,
    OTREE_REST_KEY="1234"
),
dict(
    name="security_game_total_loss",
    display_name="total_loss",
    num_demo_participants=15,
    app_sequence=[
        "consent", "survey",
                  "priming_intro", 'security_game', "ineq_manip_2b",
                  'security_game_ineq', 'attention_check', 'study_end'],
    completionlink='https://app.prolific.co/submissions/complete?cc=CWD58TF0',
    p_endowment=250,
    endowment=300,
    lost_from_attacks=100,
    p_lost_from_attacks=50,
    failed_attack=100,
    p_failed_attack=50,
    security_price=2,
    p_security_price=2,
    OTREE_REST_KEY="1234"
),
dict(
    name="security_game_vis",
    display_name="ineq_vis",
    num_demo_participants=15,
    app_sequence=[
        "consent", "survey",
                  "priming_intro", 'security_game', "ineq_manip_2b",
                  'security_game_ineq', 'attention_check', 'study_end'],
    completionlink='https://app.prolific.co/submissions/complete?cc=CWD58TF0',
    p_endowment=250,
    endowment=300,
    lost_from_attacks=100,
    p_lost_from_attacks=50,
    failed_attack=100,
    p_failed_attack=50,
    security_price=2,
    p_security_price=2,
    OTREE_REST_KEY="1234"
)
]
# for bots (need something - consent.tests?)
# otree test mysession 6

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.00, participation_fee=2.00, doc=""
)

SESSION_FIELDS = ['params']

PARTICIPANT_FIELDS =['consent', "payoff_consumed", "f_poff", "success_theft"] # necessary for passing data between apps

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='security_game_s',
        display_name='security_game_s',
        # participant_label_file='_rooms/security_game.txt',
        # use_secure_urls=True,
        # participant_label = "5",
    ),
    dict(
        name='security_game_wu',
        display_name='security_game_wu',
        # participant_label_file='_rooms/security_game.txt',
        # use_secure_urls=True,
        # participant_label = "5",
    ),
    dict(
        name='security_game_r',
        display_name='security_game_r',
        # participant_label_file='_rooms/security_game.txt',
        # use_secure_urls=True,
        # participant_label = "5",
    ),
    dict(
        name='security_game_m',
        display_name='security_game_m',
        # participant_label_file='_rooms/security_game.txt',
        # use_secure_urls=True,
        # participant_label = "5",
    ),
    dict(
        name='security_game_g',
        display_name='security_game_g',
        # participant_label_file='_rooms/security_game.txt',
        # use_secure_urls=True,
        # participant_label = "5",
    ),
    dict(
        name='security_game_um',
        display_name='security_game_um'
    )
]


# An easy thing you can do to store the Prolific PID in oTree is to set up a room without a participant label file
# (https://otree.readthedocs.io/en/latest/rooms.html) and then add ?participant_label=
# {{%PROLIFIC_PID%}} to your room-wide URL as the study URL on Prolific.
ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some versions of the security game.
"""


SECRET_KEY = '5812847175457'

INSTALLED_APPS = ['otree']

# 'django.contrib.messages'
