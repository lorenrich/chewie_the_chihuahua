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

dog_reactions = {
    'bark': [f"""
                                                                                                   
                                   /\\_/\\                                                
                                  ( o.o )                                               
                                   \\___/  --                                            
                                   |   |                                                
                                  /|   |\\                                               
    """,
    """
                                                                                                   
                                   /\\_/\\                                                
                                  ( o.o )                                               
                                   \\___/  --arf!                                        
                                   |   |                                                
                                  /|   |\\                                               
    """,
    """
                                                                                                   
                                   /\\_/\\                                                
                                  ( o.o )                                               
                                   \\___/  --arf! arf!                                   
                                   |   |                                                
                                  /|   |\\                                               
    """
    ],
    'ray_gun': [
        f"""
                                                                                                   
                                   /\\_/\\                                                
                                  ( o.o )                                               
                                   \\___/                                                
                                   |   |__|--                                           
                                  /|   |\\                                               
    """,
    """
                                                                                                   
                                   /\\_/\\                                                
                                  ( o.o )                                               
                                   \\___/                                                
                                   |   |__|-- pew!                                      
                                  /|   |\\                                               
    """,
    """
                                                                                                   
                                   /\\_/\\                                                
                                  ( o.o )                                               
                                   \\___/                                                
                                   |   |__|-- pew! pew!                                 
                                  /|   |\\                                               
    """
    ]
}


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




# Trigger frames, static
triggers_static = {
    'none': """







""",
    'fireworks': f"""
   \\ /              \\     |    /       \\ /                                
   / \\               \\    |   /        / \\                                
          \\ /         \\   |  /                                            
          / \\        ----   ----                                          
                       /  |  \\                                            
                      /   |   \\  BOOM!      \\ /                           
                     /    |    \\            / \\                           
    """,
    'bird': """


            \\__  __/                                                         
               \\/                                                            
    
    
               
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
    """],
    'bird': [
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
}




game_lose_animated = [
    """
     ________________
    |    + PET +    |                                                                                                   
    |   AMBULANCE   |              /\\_/\\                                                
    ||[][][][][][]|+|__           ( @.@ )                                               
    ||____________|    |           \\___/                                                
    |__________________|            |   |                                          
     O              O              /|   |\\                                               
    """
]










# TODO to be integrated into their respective functions

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

# Game frame outline
game_outline = "════════════════════════════════════════════════════════════════════════════"  # 76

