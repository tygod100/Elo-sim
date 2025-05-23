from Player import Player 
from nameGen import genName
import calculate
from math import floor 
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

def genPlayer():
    time = random.uniform(1, maxTime)
    life = random.uniform(0, maxLife)
    style = random.choice(list(styles.keys()))
    name = genName()
    skill = startingSkill
    elo = startingElo;
    while list(playerTimes.keys()).count(name) < 0:
        name = genName()
    
    #players.append(Player(name, skill, life, style, time, elo))
    #playerTimes.update({name: 0})
    return Player(name, skill, life, style, time, elo)
    
a = 400
b = 10
k = 36

def playAGame(player1, player2):
    probs = player1.skill + player2.skill
    winer = random.uniform(0, probs).real
    winner = ""
    print( f"{player1.name}({player1.elo}) plays a game againt {player2.name}({player2.elo}).")
    
    odd1 = calculate.calcByElo(player1.elo, player2.elo) #probability of player one winning (according to elo)
    odd2 = 1 - odd1
    
    aOdd = player1.skill/probs #the true probability of player one winning 
    eloA = abs(aOdd - odd1)
    eloA = eloA/odd1
    
    eloStake = 0

    if (winer < player1.skill.real):
        winner = player1.name
        eloStake = k * (1 - odd1)
    else:
        winner = player2.name
        eloStake = k * (1 - odd2)
        
    eloStake = abs(floor(eloStake))
        
    print(winner + " won! Taking " + str(eloStake) + " elo.")
    
    print("Elo was " + str(100 - floor(eloA * 100)) + "% accurate." )
    
    timeSpent = random.random() + 0.4
    playerTimes[player1.name] += timeSpent
    playerTimes[player2.name] += timeSpent
    
    for i in range(len(players)):
        if player1.name == players[i].name or player2.name == players[i].name:
            if (players[i].name == winner):
                players[i].elo += eloStake
                players[i].wins += 1
            else:
                players[i].elo -= eloStake
                players[i].losses += 1
    return eloA

def passDay():
    for i in range(len(players)):
        curSkill = players[i].skill
        players[i].skill += calculate.skillGain(curSkill, skillCeiling) * playerTimes[players[i].name]
        players[i].skill -= calculate.skillLoss(curSkill, skillCeiling)
        players[i].skill = players[i].skill.real
    for i in playerTimes.keys():
        playerTimes[i] = 0

def dayCheck():
    playersSillPlaying = 0
    for i in players:
        if i.time > playerTimes[i.name]:
            playersSillPlaying += 1
    return playersSillPlaying

startingPlayerCount = eval(input ("How many starting players: ")) - 1
if startingPlayerCount <= 0: startingPlayerCount = 1

skillCeiling =  eval(input ("Skill growth: "))
k =  eval(input ("K facter or calculating elo: "))

#
for i in range(startingPlayerCount):
    newPlayer = genPlayer()
    name = newPlayer.name
    players.append(newPlayer)
    playerTimes.update({name: 0})
    print (name)

while True:
    gamesPlayed = 0
    eloATotal = 0
    
    newPlayer = genPlayer()
    newPlayerName = newPlayer.name
    players.append(newPlayer)
    playerTimes.update({newPlayerName: 0})
    
    while dayCheck() > 1:
        player1 = random.choice(players)
        player2 = random.choice(players)
            
        while playerTimes[player1.name] > player1.time:
            player1 = random.choice(players)
    
        while player1.name == player2.name or playerTimes[player2.name] > player2.time:
            player2 = random.choice(players)

        eloATotal += playAGame(player1, player2)
        gamesPlayed += 1
    
    print('-'*8)
    
    for i in players:
        print(i)
        print()
        
    print('-'*8)
    for i in range(maxTime):
        totalSkill = 0
        totalElo = 0
        count = 0
        for ii in players:
            if floor(ii.time) == i:
                count += 1
                totalSkill += ii.skill
                totalElo += ii.elo
                
        if count > 0: print (f"There are {count} players who play for {i} hours a day, on average they have a skill of {totalSkill/count} and an elo of {totalElo/count}.")
    print('-'*8)
    print (newPlayerName + " started playing for the first time!")
    input( f"{gamesPlayed} games were played today. Elo was accurate {(eloATotal/gamesPlayed) * 100}% of the time")
    passDay()