import os
import sys
import termios
import time
import tty
from constants import *
from dialogue import *
from frames import *

def get_single_keypress():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        return key.lower()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def get_user_input(valid_keys=None):
    if valid_keys is None:
        valid_keys = list(GAME_KEYS.values())
    
    while True:
        key = get_single_keypress()
        if key in valid_keys:
            return key


def wait_for_key():
    get_single_keypress()


def main():
    while True:
        '''
        # Show title screen (brute force method for now)
        print(dog_title_screen)
        wait_for_key()

        # Draw dog and intro dialogue to the screen
        clear_screen()
        show_game_intro_frame(dog_state="happy")
        show_game_dialogue(text=intro)
        time.sleep(1)
        
        clear_screen()
        show_game_intro_frame(dog_state="scared")
        show_game_dialogue(text=intro_2)
        time.sleep(1)
        '''

        # Ask user to begin gameplay
        clear_screen()
        show_game_intro_frame(dog_state="none")
        show_game_dialogue(text=intro_3)
        time.sleep(1)
        choice = get_user_input([GAME_KEYS['start'], GAME_KEYS['quit']])

        if choice == GAME_KEYS['start']:
            clear_screen()
            show_game_intro_frame(dog_state="happy")
            show_game_dialogue(text="Let's go!")
            time.sleep(2)

            # Begin gameplay
            clear_screen()
            show_gameplay_frame_static(trigger="placeholder", dog_state="none")

            # Start walking
            clear_screen()
            animate_dog(dog_state='happy', animation="walking", duration=WALKING_STEPS, speed=WALKING_SPEED, trigger='placeholder')

            #Try running
            clear_screen()
            animate_dog(dog_state='scared', animation='running', duration=RUNNING_STEPS, speed=RUNNING_SPEED, trigger='placeholder')

            break

        elif choice == GAME_KEYS['quit']:
            clear_screen()
            show_game_intro_frame(dog_state="happy")
            show_game_dialogue(text="Thanks for playing!")
            break


if __name__ == "__main__":
    main()
