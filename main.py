import os
import sys
import termios
import time
import tty
from constants import *
from dialogue import *
from frames import *
from game_stats import *

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

game_state = GameState()


def main():
    def play_triggers():
        """Generate event, user chooses reaction"""

        # Start walking
        clear_screen()
        animate_dog(dog_state='happy', animation="walking", duration=WALKING_STEPS, speed=WALKING_SPEED, game_state=game_state)

        # Play trigger
        trigger = game_state.generate_new_trigger()
        clear_screen()
        animate_trigger(animation=trigger, speed=0.75, game_state=game_state)
        clear_screen()
        game_state.update_anxiety(amount=trigger_stats[trigger])

        # Check anxiety levels
        if game_state.anxiety >= 100:
            return "anxiety_too_high"

        show_gameplay_frame_static(trigger_static=trigger, dog_state='scared', game_state=game_state)
        show_game_dialogue(text=trigger_dialogue[trigger])

        # Ask user to choose reaction
        menu, option_a, option_b = game_state.generate_new_reactions()
        show_game_dialogue(text=menu)

        choice = get_user_input([GAME_KEYS['option_a'], GAME_KEYS['option_b']])
        
        # Play reaction
        if choice == GAME_KEYS['option_a']:
            time.sleep(2)
            clear_screen()
            animate_dog(dog_state='none', animation=option_a, duration=2, speed=0.75, game_state=game_state)
            game_state.update_anxiety(amount=reaction_stats[option_a]['anxiety'])
            game_state.update_courage(amount=reaction_stats[option_a]['courage'])
        elif choice == GAME_KEYS['option_b']:
            time.sleep(2)
            clear_screen()
            animate_dog(dog_state='none', animation=option_b, duration=2, speed=0.75, game_state=game_state)
            game_state.update_anxiety(amount=reaction_stats[option_b]['anxiety'])
            game_state.update_courage(amount=reaction_stats[option_b]['courage'])

        # Wrap up event
        time.sleep(2)
        clear_screen()
        game_state.update_progress(amount=25)
        show_gameplay_frame_static(trigger_static='none', dog_state='happy', game_state=game_state)
        show_game_dialogue(text="Wow! I feel a lot better!")
        time.sleep(1)

        return "continue"
    while True:
        '''
        # Show title screen (brute force method for now)
        print(dog_title_screen)
        show_game_outline()
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
            game_state.reset_progress()
            game_state.reset_anxiety()
            game_state.reset_courage()

            clear_screen() 
            show_game_intro_frame(dog_state="happy") 
            show_game_dialogue(text="Let's go!")   
            time.sleep(2)

            # Begin gameplay
            clear_screen()
            show_gameplay_frame_static(trigger_static='none', dog_state="none", game_state=game_state)

            # Main game loop
            while game_state.progress < 100 and game_state.anxiety < 100:
                # Generate events
                for i in range(4):
                    result = play_triggers()
                    if result == 'anxiety_too_high':
                        clear_screen()
                        show_gameplay_frame_static(dog_state='woozy', trigger_static='none', game_state=game_state)
                        show_game_dialogue(text="""...I...I don't feel so well""")
                        animate_dog(dog_state='none', animation="game_over", duration=1, speed=1, game_state=game_state)
                        show_game_dialogue(text="""PARAMEDIC: Help is on the way!\n\nPlay again?""")
                        play_again = get_user_input([GAME_KEYS['start'], GAME_KEYS['quit']])
                        if play_again == GAME_KEYS['quit']:
                            return
                        break
                    if game_state.progress >= 100:
                        break

                if result == 'anxiety_too_high':
                    break


            if game_state.progress >= 100:
                print("You win!")
                print("Play again?")
                play_again = get_user_input([GAME_KEYS['start'], GAME_KEYS['quit']])
                if play_again == GAME_KEYS['quit']:
                    break

        elif choice == GAME_KEYS['quit']:
            clear_screen()
            show_game_intro_frame(dog_state="happy")
            show_game_dialogue(text="Thanks for playing!")
            break

    
if __name__ == "__main__":
    main()
