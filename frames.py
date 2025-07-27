import os
import sys
from constants import *
from dialogue import *
from drawings import *
from game_stats import *


def animate_dog(dog_state, animation, duration, speed, game_state):
    eyes = dog_states[dog_state]['eyes']
    indicator = dog_states[dog_state]["indicator"]

    if animation == "walking":
        frames = get_walking_frames(dog_state)
    elif animation == "running":
        frames = get_walking_frames(dog_state)
    elif animation == 'bark':
        frames = dog_reactions['bark']
    elif animation == 'ray_gun':
        frames = dog_reactions['ray_gun']
    elif animation == 'game_over':
        frames = game_over_animated
    elif animation == 'you_win':
        frames = you_win_animated

    for i in range(0, duration):
        for frame in frames:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            show_gameplay_frame_animated_dog(dog_state, game_state)
            print(frame)
            show_game_outline()
            time.sleep(speed)

def animate_trigger(animation, speed, game_state):
    frames = triggers_animated[animation]

    for frame in frames:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        show_gameplay_frame_animated_trigger(game_state)
        print(frame)
        print(render_dog(dog_state='none'))
        show_game_outline()
        time.sleep(speed)


class GameFrame:
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        self.content = []

    def add_line(self, text: str="", center=True):
        self.content.append(text.center(self.SCREEN_WIDTH))

    def add_padding(self, lines=1):
        for i in range(0, lines):
          self.add_line("")

    def add_multi_line_block(self, text_block: str, center=False):
        lines = text_block.split('\n')
        for line in lines:
            self.add_line(line, center=center)

    def character_speech(self, text, DOG_SPEECH_SPEED, center=False):
        """Display dialogue with typewriter effect"""
        lines = text.split('\n')
        if text is None:
            text = ""
        for line in lines:
            self.content.append(line)
        for character in text:
            if character in '.!?':
                time.sleep(DOG_SPEECH_SPEED * 10)
            print(character, end="", flush=True)
            time.sleep(DOG_SPEECH_SPEED)

    def add_game_stat(self, type: str="",  center=False):
        self.content.append(type)

    def clear_screen():
      """Clear screen according to user's operating system"""
      if os.name == 'nt':
          os.system('cls')
      else:
          os.system('clear')

    def render(self):
        for item in self.content:
            print(item)
        
        # Clear content list after rendering
        self.content = []

def clear_screen():
      """Clear screen according to user's operating system, callable outside of GameFrame class"""
      if os.name == 'nt':
          os.system('cls')
      else:
          os.system('clear')


# Functions for different game frames
def show_title_frame():
    # Not currently used until I fix spacing issue
    frame = GameFrame(SCREEN_WIDTH, SCREEN_HEIGHT)
    frame.add_padding(2)
    frame.add_multi_line_block(text_block=render_dog_title("title"), center=False)
    frame.add_padding(2)
    frame.render()
    input()

def show_game_outline():
    frame = GameFrame(SCREEN_WIDTH, SCREEN_HEIGHT)
    frame.add_line(game_outline)
    frame.render()

def show_game_intro_frame(dog_state):
    frame = GameFrame(SCREEN_WIDTH, SCREEN_HEIGHT)
    frame.add_line(text=game_outline)
    frame.add_padding(13)
    dog_render = render_dog(dog_state)
    frame.add_multi_line_block(text_block=dog_render, center=False)
    frame.add_line(text=game_outline)
    frame.render()

def show_game_dialogue(text):
    frame = GameFrame(SCREEN_WIDTH, SCREEN_HEIGHT)
    frame.add_padding(1)
    frame.character_speech(text, DOG_SPEECH_SPEED, center=False)

def show_gameplay_frame_static(trigger_static, dog_state, game_state):
    """Standard game screen, static dog"""
    frame = GameFrame(SCREEN_WIDTH, SCREEN_HEIGHT)
    trigger_drawing = triggers_static[trigger_static]
    
    # Top of frame with game stats
    frame.add_line(text=game_outline)
    frame.add_game_stat(type=game_state.get_progress_bar())
    frame.add_game_stat(type=game_state.get_anxiety_bar())
    frame.add_game_stat(type=game_state.get_courage_bar())

    # Game event (trigger)
    frame.add_padding(1)
    frame.add_multi_line_block(text_block=trigger_drawing, center=False)

    # Dog
    dog_render = render_dog(dog_state)
    frame.add_multi_line_block(text_block=dog_render, center=False)
    frame.add_line(text=game_outline)

    frame.render()

def show_gameplay_frame_animated_dog(dog_state, game_state):
    """Standard game screen, animated dog"""
    frame = GameFrame(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Top of frame with game stats
    frame.add_line(text=game_outline)
    frame.add_game_stat(type=game_state.get_progress_bar())
    frame.add_game_stat(type=game_state.get_anxiety_bar())
    frame.add_game_stat(type=game_state.get_courage_bar())
    frame.add_padding(2)

    # Add spacing for game event (trigger)
    frame.add_padding(8)

    frame.render()

def show_gameplay_frame_animated_trigger(game_state):
    """Standard game screen, animated trigger"""
    frame = GameFrame(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Top of frame with game stats
    frame.add_line(text=game_outline)
    frame.add_game_stat(type=game_state.get_progress_bar())
    frame.add_game_stat(type=game_state.get_anxiety_bar())
    frame.add_game_stat(type=game_state.get_courage_bar())
    frame.add_padding(1)

    frame.render()