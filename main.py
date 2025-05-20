from Player import Player 
from nameGen import genName
import random

print("hello world")

styles = {"rock": 1, "paper" : 2, "blade" : 0}

startingElo = 1500
startingSkill = 1
skillCeiling = 5 #not the max; multiplier

maxTime = 6
maxLife = 0.3

players = []
playerTimes = {"nobody": 0}

#players.append(Player("Tyler Hom", startingSkill + 1, 0, 1, maxTime))
#playerTimes.append("nobody")

#print(styles.keys())

a = 400
b = 10
k = 36

startingPlayerCount = eval(input ("How many players: "))

#need to urn this into a fun
for i in range(startingPlayerCount):
    time = random.uniform(1, maxTime)
    life = random.uniform(0, maxLife)
    style = random.choice(list(styles.keys()))
    name = genName()
    skill = startingSkill
    elo = startingElo;
    while list(playerTimes.keys()).count(name) < 0:
        name = genName()
    
    players.append(Player(name, skill, life, style, time, elo))
    playerTimes.update({name: 0})
    print (name)

for i in players:
    print(i)