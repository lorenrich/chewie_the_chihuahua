SCREEN_WIDTH = 65
SCREEN_HEIGHT = 25

WALKING_SPEED = 0.5
WALKING_STEPS = 10

RUNNING_SPEED = 0.2
RUNNING_STEPS = 15

DOG_SPEECH_SPEED = 0.01  # Once ready for actual gameplay, change to 0.05 

dog_states = {
    "none": {"eyes": "o", "indicator": ""},
    "title": {"eyes": "o", "indicator": ""},
    "happy": {"eyes": "^", "indicator": ""},
    "scared": {"eyes": "0", "indicator": "!"},
    "dead": {"eyes": "x", "indicator": "X"}
}

dog_title_screen = f"""

      /\\_/\\
     ( ^.^ )      Chewie the Chihuahua
      \\___/
      |   |       Press ENTER to begin
     /|   |\\
______________________________________
    """

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

def walking_dog(frames, steps=0):
    for i in range(0, steps):
        for frame in frames:
            os.system('cls')
            print(frame)
            time.sleep(0.5)

def ray_gun_dog(dog_ray_gun_frames, shots=0):
    for i in range(0, shots):
        for frame in dog_ray_gun_frames:
            os.system('cls')
            print(frame)
            time.sleep(0.5)

def barking_dog(dog_barking_frames, barks=0):
    for i in range(0, barks):
        for frame in dog_barking_frames:
            os.system('cls')
            print(frame)
            time.sleep(0.5)

