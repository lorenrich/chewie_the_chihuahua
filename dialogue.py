import time
from constants import *

def character_speech(text, DOG_SPEECH_SPEED):
    for character in text:
        if character in '.!?':
            time.sleep(DOG_SPEECH_SPEED * 10)
        print(character, end="", flush=True)
        time.sleep(DOG_SPEECH_SPEED)
    return

# Text variables for character speech
intro = "Hi. I'm Chewie. \nI'm a 5-pound Chihuahua who struggles with anxiety. It's hard not to be afraid when everything is bigger " \
        "than you. \nMy owner says I need to go for a walk...the thought of it terrifies me."

intro_2 = "If I face my fears appropriately, I can go home and have a treat.\nIf I make the wrong choices, my anxiety could get too "\
          "high. \nI'm going to let you make the decisions."

intro_3 = "...Are you ready to go?"""