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