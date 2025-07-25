import os
import sys
import time
from constants import *
from dialogue import *
from frames import *

def main():
    # Draw dog and intro dialogue to the screen
    render_dog(happy_eyes, happy_emotion_indicator)
    character_speech(intro, DOG_SPEECH_SPEED)




if __name__ == "__main__":
    main()
