import time
from constants import *


# Text variables for character speech
intro = "Hi. I'm Chewie. \nI'm a 5-pound Chihuahua who struggles with anxiety. It's hard not to "\
    "\nbe afraid when everything is bigger than you.\nMy owner says I need to go for a walk"

intro_2 = "...the thought of it terrifies me.\nIf I face my fears, I can go home "\
    "and have a treat.\nIf my anxiety gets too high, I'll get sick."

intro_3 = f"...Are you ready to go?\n\nPress {GAME_KEYS['start']} to begin or {GAME_KEYS['quit']} to quit  "

game_over = """...I...I don't feel so well...I think my anxiety got the best me."""

game_over_2 = """PARAMEDIC: Help is on the way!\n\nPlay again?\n"""

you_win = """...Thank goodness it's over!  Great work!\nI'm going to have myself a well deserved treat.\n\nPlay again?\n"""

# Dog  dialogue reactions to triggers
trigger_dialogue = {
    "blowing_leaf": "Oh...a leaf blowing in the wind...coming straight for me...",
    "fireworks": "HOLY CRAP!  Fireworks!!!!!",
    "bird": "Is that a hawk?  ...he looks hungry...",
    "child": "Oh no, small child. \nPlease don't want to pet me.  Please don't want to pet me. Please don't want to pet me.",
    "human": "Shoot...scary human...",
    "other_dog": "Hello other dog.  No, I don't want to be your friend.",
    "lightning": "Oh no, thunderstorm!",
    "people": """Please don't want to pet...ah crap.""",
}

reaction_menu = {
    'bark': 'Bark your head off',
    'ray_gun': """Shoot 'em with a ray gun""",
    'play_dead': "Play dead",
    'play_it_cool': "Play it cool"
}

