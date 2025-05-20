import random

#first names from https://weakpass.com/wordlists/common_names.txt
#last  names from https://lorepublication.com/writing-aids/fantasy-words-list-fantasy-writers/

file = open("firstNames.txt")
nameList = file.readlines()
file.close()
firstNames = tuple(nameList)
file = open("lastNames.txt")
nameList = file.readlines()
lastNames = tuple(nameList)
file.close()
del nameList

def genName():
    return (random.choice(firstNames) + " " + random.choice(lastNames).replace("cy\n", "ski")).replace('\n', '').title()
