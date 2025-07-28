import os
import time
from constants import *

dog_frame_title = f"""
                                                                                                 
                                   /\\_/\\                                                
                                  ( ^.^ )         Chewie the Chihuahua                        
                                   \\___/                                                
                                   |   |          press any key to start            
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
    ],
    'play_dead': [
        """


        
                                   /\\_/\\                                                
                                  ( X.X ) __|__|                                               
                                   \\___/ __|__|                                                                                 
""",
"""


        
                                   /\\_/\\                                                
                                  ( X.X ) __|__|     ...                                       
                                   \\___/ __|__|                                                                                 
""",
"""


        
                                   /\\_/\\                                                
                                  ( X.X ) __|__|     ...did it work?                              
                                   \\___/ __|__|                                                                                 
"""
    ],
    'play_it_cool':[
        """
                                                                                                   
                                   /\\_/\\                                                
                                  (-●.●-)                                               
                                   \\___/                                                
                                   |   |                                 
                                  /|   |\\                                               
    """,
    """
                                                                                                   
                                   /\\_/\\                                                
                                  (-●.●-)                                               
                                   \\___/     *whistles                                  
                                   |   |                                 
                                  /|   |\\                                               
    """,
    """
                                                                                                   
                                   /\\_/\\                                                
                                  (-●.●-)                                               
                                   \\___/     *whistles                                  
                                   |   |                                 
                                  /|   |\\                                               
    """
    ]
}


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
    
    
               
    """,
    'lightning': """
                                   /                                                             
                                  /___                                                  
                                     /                                                                   
                                    /                                                                      
                                   /                                                        
                                  /                                         
   
     """,
    'people': """

                                                                             
                                                     --Can we pet your dog? 
                                                                             
                                                                             


""",
    'game_over': """
    _________________                                                                                                   
    |               |              /\\_/\\                                                
    ||   + PET +  |+|__           ( @.@ )                                               
    ||  AMBULANCE      |           \\___/                                                
    |__________________|           |   |                                           
     O              O             /|   |\\                                                
    """,
    'you_win': """
                                                                            
                                   /\\_/\\                                    
                                  ( ^.^ )          __    __                 
                                   \\___/          /  \\__/  \\                
                                   |   |         |   BONE   |               
                                  /|   |\\         \\__/  \\__/                
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
    ],
    'lightning': [
        """

           /                                                                                     
          /__                                                                          
              /                                                                   
             /                                                                      
            /                                                        
                                                                          
    """,
    """

                                   /                                                             
                                  /___                                                  
                                     /                                                                   
                                    /                                                                      
                                   /                                                        
                                  /                                         
    """
    ],
    'people': [
        """

                                                   --Aww! Look at that dog! 
                                                                            
                                                                             
                                                                             


""",
"""

                                                   --Aww! Look at that dog! 
                                                                            
                                                                             
                                                                             


""",
"""

                                                                             
                                                                             
                                                            --What a cutie! 
                                                                             


""",
"""

                                                                             
                                                                             
                                                            --What a cutie! 
                                                                             


""",
"""

                                                                             
                                                                             
                                                                             
                                             --Are you sure it's not a rat? 


""",
"""

                                                                             
                                                                             
                                                                             
                                             --Are you sure it's not a rat? 


""",
"""

                                                                             
                                                     --Can we pet your dog? 
                                                                             
                                                                             


""",
"""

                                                                             
                                                     --Can we pet your dog? 
                                                                             
                                                                             


"""
    ]
}


you_win_animated = [
    """
                                                                            
                                   /\\_/\\                                    
                                  ( ^.^ )          __    __                 
                                   \\___/          /  \\__/  \\                
                                   |   |         |   BONE   |               
                                  /|   |\\         \\__/  \\__/                
    """
]  # Not yet animated



game_over_animated = [
    """
_________________                                                                                                       
|               |                  /\\_/\\                                                
||   + PET +  |+|__               ( @.@ )                                               
||  AMBULANCE      |               \\___/                                                
|__________________|               |   |                                           
 O              O                 /|   |\\                                                
    """,
    """
  _________________                                                                                                     
  |               |                /\\_/\\                                                
  ||   + PET +  |+|__             ( @.@ )                                               
  ||  AMBULANCE      |             \\___/                                                
  |__________________|             |   |                                           
   O              O               /|   |\\                                                
    """,
    """
    _________________                                                                                                   
    |               |              /\\_/\\                                                
    ||   + PET +  |+|__           ( @.@ )                                               
    ||  AMBULANCE      |           \\___/                                                
    |__________________|           |   |                                           
     O              O             /|   |\\                                                
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

