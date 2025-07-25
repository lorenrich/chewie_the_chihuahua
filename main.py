import os
import sys
import time
from constants import *
from dialogue import *
from frames import *

def main():
    # Draw dog and intro dialogue to the screen
    clear_screen()
    render_dog(happy_eyes, happy_indicator)
    character_speech(intro, DOG_SPEECH_SPEED)
    clear_screen()

    render_dog(scared_eyes, scared_indicator)
    character_speech(intro_2, DOG_SPEECH_SPEED)
    clear_screen()

    render_dog(no_expression_eyes, no_expression_indicator)
    character_speech(intro_3, DOG_SPEECH_SPEED)
    clear_screen()





if __name__ == "__main__":
    main()
