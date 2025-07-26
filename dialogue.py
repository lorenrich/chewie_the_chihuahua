import time
from constants import *


# Text variables for character speech
intro = "Hi. I'm Chewie. \nI'm a 5-pound Chihuahua who struggles with anxiety. It's hard not to "\
    "\nbe afraid when everything is bigger than you.\nMy owner says I need to go for a walk"

intro_2 = "...the thought of it terrifies me.\nIf I face my fears appropriately, I can go home "\
    "and have a treat.\nIf I make the wrong choices, my anxiety could get too high."

intro_3 = f"I'm going to let you make the decisions...Are you ready to go?\n\nPress {GAME_KEYS['start']} to begin or {GAME_KEYS['quit']} to quit"

# Dog  dialogue reactions to triggers
trigger_reactions = {
    "blowing_leaf": "Oh...a leaf blowing in the wind...coming straight for me...",
    "firework": "HOLY CRAP!  Fireworks!!!!!",
    "bird": "Is that a hawk?  Man...he looks hungry...",
    "child": "Oh no, small child. \nPlease don't want to pet me.  Please don't want to pet me. Please don't want to pet me.",
    "human": "Shoot...scary human...",
    "other_dog": "Hello other dog.  No, I don't want to be your friend."
}