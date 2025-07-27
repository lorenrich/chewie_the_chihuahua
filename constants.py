SCREEN_WIDTH = 76
SCREEN_HEIGHT = 25

GAME_KEYS = {
    'start': 'y',
    'quit': 'q',
    'option_a': 'a',
    'option_b': 'b',
    'option_c': 'c'
}

WALKING_SPEED = 0.4
WALKING_STEPS = 3

RUNNING_SPEED = 0.1
RUNNING_STEPS = 7

DOG_SPEECH_SPEED = 0.01  # Once ready for actual gameplay, change to 0.05 

dog_states = {
    "none": {"eyes": "o", "indicator": ""},
    "title": {"eyes": "o", "indicator": ""},
    "happy": {"eyes": "^", "indicator": ""},
    "scared": {"eyes": "0", "indicator": "!"},
    "dead": {"eyes": "x", "indicator": "X"},
    'woozy': {"eyes": "@", 'indicator': "~"}
}

BARKING_LOOP = 2
BARKING_SPEED = 0.1

