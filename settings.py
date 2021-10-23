# from django.contrib import messages
from os import environ
from os import popen

SESSION_CONFIGS = [
    dict(
        name='security_game_pretest',
        app_sequence=['consent', 'intro', 'security_game_pretest', 'questionnaires', 'attention_check', 'payment_info'],
        num_demo_participants=1,
        completionlink='https://app.prolific.co/submissions/complete?cc=7A7A0682',
        oTree_version_used=popen('otree --version').read().strip()
    ),
    dict(
        name='intro', app_sequence=['intro', 'payment_info'], num_demo_participants=1,
    ),
    dict(
        name='inequality_visibility_security',
        app_sequence=['inequality_visibility', 'security_game'],
        num_demo_participants=20,
        completionlink='https://app.prolific.co/submissions/complete?cc=7A7A0682',
        endowment=12345435,
        lost_from_attacks=10002,
        failed_attack=13232
    ),

    dict(
        name="security_game_merit",
        display_name="meritocracy_manip",
        num_demo_participants=1,
        app_sequence=["slider_task", 'security_game'],

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

SESSION_FIELDS = ['params','svars']

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='security_game',
        display_name='security_game',
        # participant_label_file='_rooms/security_game.txt',
        # use_secure_urls=True,
        # participant_label = "5",
    ),
    dict(
        name='security_game_pretest',
        display_name='security_game_pretest',
        # participant_label_file='_rooms/security_game.txt',
    ),
]


# An easy thing you can do to store the Prolific PID in oTree is to set up a room without a participant label file
# (https://otree.readthedocs.io/en/latest/rooms.html) and then add ?participant_label=
# {{%PROLIFIC_PID%}} to your room-wide URL as the study URL on Prolific.
ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '5812847175457'

INSTALLED_APPS = ['otree']

# 'django.contrib.messages'
