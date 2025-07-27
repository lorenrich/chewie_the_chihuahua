import random
from dialogue import reaction_menu

trigger_stats = {
    'bird': 10,
    'blowing_leaf': 20,
    'fireworks': 30
}

reaction_stats = {
    'bark': {'anxiety': -20, 'courage': 20},
    'ray_gun': {'anxiety':  -50, 'courage': 40}
}

class GameState:
    def __init__(self):
        self.current_dog_event = None
        self.available_triggers = ['fireworks', 'bird']
        self.available_reactions = ['bark', 'ray_gun']
        self.progress = 0
        self.anxiety = 25
        self.courage = 25

        
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
    
    def update_progress(self, amount):
        self.progress += amount
        return self.progress
    
    def update_anxiety(self, amount):
        self.anxiety += amount
        if self.anxiety < 0:
            self.anxiety = 0
        elif self.anxiety > 100:
            self.anxiety = 100
        return self.anxiety
    
    def update_courage(self, amount):
        self.courage += amount
        if self.courage < 0:
            self.courage = 0
        elif self.courage > 100:
            self.courage = 100
        return self.courage
    
    def get_progress_bar(self):
        return "Progress " + "█" * (self.progress // 10) + "░" * (10 - self.progress // 10) + f" {self.progress}%"
    
    def get_anxiety_bar(self):
        return "Anxiety  " + "█" * (self.anxiety // 10) + "░" * (10 - self.anxiety // 10) + f" {self.anxiety}%"
        
    def get_courage_bar(self):    
        return "Courage  " + "█" * (self.courage // 10) + "░" * (10 - self.courage // 10) + f" {self.courage}%"

    def reset_progress(self):
        self.progress = 0
        return self.progress
    
    def reset_anxiety(self):
        """Randomly select a starting point for anxiety.  Not every day is a good day"""
        self.anxiety = random.randint(0, 50)
        return self.anxiety
    
    def reset_courage(self):
        """Randomly select a starting point for courage.  Not every day is a good day"""
        self.courage = random.randint(1, 50)
        return self.courage