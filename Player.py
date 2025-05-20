from math import floor 

'''

skill is the player's base line for wining. is seprent from elo
life is the chanshe that the player is haveing a bed day
time is how much time the player is willing to spend playing

'''

class Player:
    elo = 1500
    skill = 100
    name = "mr test"
    life = 0
    style = 1
    time = 10
    def __init__(self, name):
        self.name = name
    def __init__(self, name, skill, life, style, time, elo):
        self.name = name
        self.skill = skill
        self.life = life
        self.style = style
        self.time  = time
        self.elo = elo
    def __str__(self):
        life = self.life
        lifeS = "great!"
        if life > 0.9:
            lifeS = "god awful!"
        elif life > 0.7:
            lifeS = "poor."
        elif life > 0.4:
            lifeS = "ok."
        elif life > 0.1:
            lifeS = "good."
        
        return f"{self.name} has an elo of ({self.elo}) with a skill of ({self.skill}).\nThey are willing to spent {floor(self.time)} hours on gaming and their life situation is {lifeS}"