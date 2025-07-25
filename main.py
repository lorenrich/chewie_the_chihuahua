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
    render_text_frame(text=intro)
    time.sleep(0.1)
    clear_screen()

    # TODO left off here, it doesn't matter if you start with happy or scared, the following one throws an error where lines in
    # TODO multi_line_block is getting passed NoneType
    show_game_intro_frame(dog_state="scared")
    render_text_frame(text=intro_2)
    time.sleep(0.1)
    clear_screen()

    show_game_intro_frame(dog_state="none")
    render_text_frame(text=intro_3)
    time.sleep(0.1)
    input()





if __name__ == "__main__":
    main()
