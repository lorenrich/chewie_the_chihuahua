import os
import time
from constants import *


# Dog drawings, static
dog_title_screen = f"""

      /\\_/\\
     ( ^.^ )      Chewie the Chihuahua
      \\___/
      |   |       Press any key to begin
     /|   |\\
    """

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


# Dog drawings, actioned; formatted as functions to allow successful passing of emotions to each action
def get_walking_frames(dog_state):
    eyes = dog_states[dog_state]['eyes']
    indicator = dog_states[dog_state]["indicator"]
    return [
    f"""
                                     {indicator}                                                   
                                   /\\_/\\                                                
                                  ( {eyes}.{eyes} )                                               
                                   \\___/                                                
                                   |   |                                                
                                  /|   |\\                                              
    """,
    f"""
                                     {indicator}                                                   
                                   /\\_/\\                                                
                                  ( {eyes}.{eyes} )                                               
                                   \\___/                                                
                                   |   |                                                
                                  /    |\\                                              
    """,
    f"""
                                     {indicator}                                                   
                                   /\\_/\\                                                
                                  ( {eyes}.{eyes} )                                               
                                   \\___/                                                
                                   |   |                                                
                                   |\\  /                                               
    """
]


# Dog reactions to triggers, static and actioned
ray_gun = [
    """
       /\\_/\\
      ( o.o )
       \\___/
       |   |__|--
      /|   |
      __________
    """,
    """
       /\\_/\\
      ( o.o )
       \\___/
       |   |__|-- pew!
      /|   |\\
      __________
    """,
    """
       /\\_/\\
      ( o.o )
       \\___/
       |   |__|-- pew! pew!
      /|   |\\
      __________
    """
]

barking = [
    """
       /\\_/\\
      ( o.o )
       \\___/
       |   |
      /|   |\\
      __________
    """,
    """
       /\\_/\\
      ( o.o )
       \\___/ -- arf!
       |   |
      /|   |\\
      __________
    """,
    """
       /\\_/\\
      ( o.o )
       \\___/ -- arf! arf!
       |   |
      /|   |\\
      __________
    """
]



# Trigger frames, static
triggers_static = {
    'none': '',
    'fireworks': f"""
   \\ /              \\     |    /       \\ /                                
   / \\               \\    |   /        / \\                                
          \\ /         \\   |  /                                            
          / \\        ----   ----                                          
                       /  |  \\                                            
                      /   |   \\  BOOM!      \\ /                           
                     /    |    \\            / \\                           
    """
}


# Trigger frames, animated
triggers_animated = {
    'fireworks': ["""
    \\ /                                                                   
    / \\  pop!                                                              
                                                                          
                                                                          
                                                                          
                                             \\ /                          
                                             / \\  pop!                    
    """,
    """
    \\ /                                 \\ /                               
    / \\                                 / \\  pop!                         
           \\ /                                                            
           / \\ pop!                                                       
                                                                          
                                             \\ /                          
                                             / \\                          
    """,
    """
    \\ /              \\     |    /       \\ /                               
    / \\               \\    |   /        / \\                               
           \\ /         \\   |  /                                           
           / \\        ----   ----                                         
                        /  |  \\                                           
                       /   |   \\  BOOM!      \\ /                          
                      /    |    \\            / \\                          
    """]
}

























blowing_leaf = [
    """
       /\\
    |\\|  |/|
    |      |
     \\____/
        |
    """,
    """
         /\\
      |\\|  |/|
      |      |
       \\____/
          |
    """,
    """
           /\\
        |\\|  |/|
        |      |
         \\____/
            |
    """
]

bird = [
    """
    
      __   __
     /   \\/  \\
    
    
    """,
    """
    
        \\__  __/
           \\/  
    
    
    """,
    """
    
           __   __
          /   \\/  \\
    
    
    """,
    """
    
            \\__  __/
               \\/  
    
    
    """
]

# Game frame outline
game_outline = "═══════════════════════════════════════════════════════════════════════════"  # 75

