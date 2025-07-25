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


dead_eyes = "x"
dead_indicator = "X"

happy_eyes = "^"
happy_indicator = ""

no_expression_eyes = "o"
no_expression_indicator = ""

scared_eyes = "0"
scared_indicator = "!"