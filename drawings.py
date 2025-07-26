from constants import *

# Dog drawings, static
dog_title_screen = f"""

      /\\_/\\
     ( ^.^ )      Chewie the Chihuahua
      \\___/
      |   |       Press any key to begin
     /|   |\\
______________________________________
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

# Dog drawings, actioned
walking_dog_frames = [
"""
       /\\_/\\
      ( o.o )
       \\___/
       |   |
      /|    |\\
      __________
    """,
"""
       /\\_/\\
      ( o.o )
       \\___/
       |   |
      |\\   /
      __________
    """
]

walking_dog_frames2 = [
    """
   /\\_/\\
  ( o.o )
   \\___/
   |   |
  /|   |\\
    """,
    """
   /\_/\\
  ( o.o )
   \\___/
   |   |
  /    |\\
    """,
    """
   /\\_/\\
  ( o.o )
   \\___/
   |   |
  |\\   /
    """
]

# Dog reactions to triggers, static and actioned
dog_ray_gun_frames = [
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

dog_barking_frames = [
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

# Trigger frames
blowing_leaf_frames = [
    """
       /\\
    |\|  |/|
    |      |
     \\____/
        |
    """,
    """
         /\\
      |\|  |/|
      |      |
       \\____/
          |
    """,
    """
           /\\
        |\|  |/|
        |      |
         \\____/
            |
    """
]

firework_frames = [
    """
           
            
     \\ /    
     / \\
     pop!        
            
           
    """,
    """
                             \\ / pop!
                             / \\
     \\ /
     / \\
             
           
           
    """,
    """
           \\    |    /       \\ /
            \\   |   /        / \\
     \\ /     \\  |  /
     / \\   ----   ----
             /  |  \\
            /   |   \\  BOOM!
           /    |    \\ 
    """
]

bird_frames = [
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

