# Dog frame, no expression

def render_dog(eyes, emotion_indicator):
    dog_frame = f"""
      {emotion_indicator}
    /\\_/\\
   ( {eyes}.{eyes} )
    \\___/
    |   |
   /|   |\\
    __________
    """
    print(dog_frame)


happy_eyes = "^"
happy_emotion_indicator = ""

dog_no_expression = """
   /\\_/\\
  ( o.o )
   \\___/
   |   |
  /|   |\\
  __________
"""

dog_happy = """
   /\\_/\\
  ( ^.^ )
   \\___/
   |   |
  /|   |\\
  __________
"""

dog_scared = """
     !
   /\\_/\\
  ( 0.0 )
   \\___/
   |   |
  /|   |\\
  __________
"""

dog_dead = """
   /\\_/\\
  ( x.x )
   \\___/
   |   |
  /|   |\\
  __________
"""