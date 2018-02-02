#Rock/Paper/Scissors game
#Determine how many time you wanna play with computer.
#Inform who won after each round.
#Statistics for the end of game.

import random

choicesList = ['R', 'P', 'S']
userStats= {'win':0, 'lost':0, 'tie':0}
winnerCombinations = {'SP', 'PR', 'RS'}

userChoice = ""
compChoice = ''

rounds = 0

while True:
    try:
        rounds = int(input("How many rounds you wanna play: "))
        if rounds>0:
            break
        else:
            raise ValueError
    except ValueError:
        print("Wrong input. Enter an integer value > 0.")


for i in range(1, rounds + 1):
    print("***ROUND %d ***" %i)
    compChoice = random.choice(choicesList)
    userChoice = str(input("P for Paper, S for scissors, R for Rock.")).upper()

    if userChoice in choicesList:
        if userChoice == compChoice:
            userStats['tie'] += 1
            print("TIE!")
        elif userChoice + compChoice in winnerCombinations:
            userStats['win'] += 1
            print("You Win! Computer choose %s" %compChoice)
        else:
            userStats['lost'] += 1
            print("You lost! Computer choose %s" %compChoice)
    else:
        print("Wrong input, you have lost this round!")
        userStats['lost'] = userStats['lost'] + 1

print("You won %d times, lost %d times, tie %d times." % (userStats['win'], userStats['lost'], userStats['tie']))