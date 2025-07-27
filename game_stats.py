import random
from dialogue import reaction_menu

# Beginning stats
progress = 0
anxiety = 25
courage = 25

# Stat bars
progress_bar = "Progress " + "█" * (progress // 10) + "░" * (10 - progress // 10) + f" {progress}%"
anxiety_bar = "Anxiety  " + "█" * (anxiety // 10) + "░" * (10 - anxiety // 10) + f" {anxiety}%"
courage_bar = "Courage  " + "█" * (courage // 10) + "░" * (10 - courage // 10) + f" {courage}%"


trigger_stats = {
    'bird': 10,
    'blowing_leaf': 20,
    'fireworks': 30
}

reaction_stats = {
    'barking': {'anxiety': -20, 'courage': 20},
    'ray_gun': {'anxiety':  -50, 'courage': 40}
}

class GameState:
    def __init__(self):
        self.current_dog_event = None
        self.available_triggers = ['fireworks', 'bird']
        self.available_reactions = ['bark', 'ray_gun']
        
    def generate_new_trigger(self):
        self.current_dog_event = random.choice(self.available_triggers)
        return self.current_dog_event
    
    def generate_new_reactions(self):
        """Generate multiple options for the user to choose from"""
        self.unused_reactions = self.available_reactions.copy()
        reaction_list = []

        for i in range(2):  # Will change to 4 when we have enough reactions
            self.current_reactions = random.choice(self.unused_reactions)
            reaction_list.append(self.current_reactions)
            self.unused_reactions.remove(self.current_reactions)

        menu = f"\nWhat should I do?\n"
        menu += f"\nA. {reaction_menu[reaction_list[0]]}\n"
        menu += f"B. {reaction_menu[reaction_list[1]]}\n"
        
        return menu, reaction_list[0], reaction_list[1]