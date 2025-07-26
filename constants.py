SCREEN_WIDTH = 65
SCREEN_HEIGHT = 25

GAME_KEYS = {
    'start': 'y',
    'quit': 'q',
    'option_a': 'a',
    'option_b': 'b',
    'option_c': 'c'
}

WALKING_SPEED = 0.4
WALKING_STEPS = 5

RUNNING_SPEED = 0.1
RUNNING_STEPS = 7

DOG_SPEECH_SPEED = 0.01  # Once ready for actual gameplay, change to 0.05 

dog_states = {
    "none": {"eyes": "o", "indicator": ""},
    "title": {"eyes": "o", "indicator": ""},
    "happy": {"eyes": "^", "indicator": ""},
    "scared": {"eyes": "0", "indicator": "!"},
    "dead": {"eyes": "x", "indicator": "X"}
}


# TODO Migrate this to a single function?
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

