import os
import sys
from constants import *
from dialogue import *


def render_dog(dog_state):
    eyes = dog_states[dog_state]["eyes"]
    indicator = dog_states[dog_state]["indicator"]

    dog_frame = f"""
  {indicator}
 /\\_/\\
 ( {eyes}.{eyes} )
 \\___/
  |   |
 /|   |\\
    """

    return dog_frame


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

def show_game_intro_frame(dog_state):
    frame = GameFrame(SCREEN_WIDTH, SCREEN_HEIGHT)
    frame.add_padding(2)
    dog_render = render_dog(dog_state)
    frame.add_multi_line_block(text_block=dog_render, center=True)
    frame.render()

def show_game_intro_frame2(text):
    frame = GameFrame(SCREEN_WIDTH, SCREEN_HEIGHT)
    frame.add_padding(2)
    frame.character_speech(text, DOG_SPEECH_SPEED, center=False)