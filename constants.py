import os

WALKING_SPEED = 0.5
WALKING_STEPS = 10

RUNNING_SPEED = 0.2
RUNNING_STEPS = 15

DOG_SPEECH_SPEED = 0.05

def clear_screen():
    # Clear screen according to user's operating system
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')