import random
import os
os.system("cls")

def getRandomWord(word, rTemp1, rTemp2):
    rand1 = 0
    rand2 = 0

    while (rand1 == rand2 or rTemp1 == rand1 or rTemp2 == rand2):
        rand1 = random.randint(0,len(word)-1)
        rand2 = random.randint(0,len(word)-1)
    
    rTemp1 = rand1
    rTemp2 = rand2
    return [rand1, rand2]

def scramble(word):
    rTemp1 = 0
    rTemp2 = 0
    for c in range(len(word)):
        for cc in range(len(word)):
            rand = getRandomWord(word, rTemp1, rTemp2)

            listWord = list(word)
            temp = word[rand[0]]
            listWord[rand[0]] = listWord[rand[1]]
            listWord[rand[1]] = temp
            
            rTemp1 = rand[0]
            rTemp2 = rand[1]
        return ''.join(listWord)

loop = True
while(loop):
    print("Please enter a word")
    word = input()

    if(word.lower() == 'n'): 
        loop = False
        break

    newWord = scramble(word)
    print(newWord)

