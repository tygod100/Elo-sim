import math
b = 10
a = 100

#Calculates the chance of player 1 winning by elo
#enter the elo of each player
def calcByElo (player1, player2):
    odd = 0 #odds of player one winning (according to elo)
    
    odd = 1 / (1 + pow(b, (player2 - player1)/a ))
    #print (odd1)
    return odd


# skill* 0.5^skill/multiplier
def skillGain (skill, multiplier):
    gained = 0
    gained = skill #* multiplier
    lowerer = pow(0.5, skill/multiplier)
    gained = gained * lowerer
    return gained

# ( (skill - multiplier)/multiplier )^0.5
def skillLoss (skill, multiplier):
    loss = skill - multiplier
    loss = loss/multiplier
    loss = pow(loss, 0.5)
    
    return loss