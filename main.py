import os
import sys
import time
from constants import *
from dialogue import *
from frames import *

def main():
    # Show title screen (brute force method for now)
    print(dog_title_screen)
    input()

    # Draw dog and intro dialogue to the screen
    clear_screen()
    show_game_intro_frame(dog_state="happy")
    show_game_intro_frame2(text=intro)
    time.sleep(0.1)
    clear_screen()

    show_game_intro_frame(dog_state="scared")
    show_game_intro_frame2(text=intro_2)
    time.sleep(0.1)
    clear_screen()

    show_game_intro_frame(dog_state="none")
    show_game_intro_frame2(text=intro_3)
    time.sleep(0.1)
    input()





if __name__ == "__main__":
    main()
