#Hangman game

import random
import re

hangmanState = [
#0
"""
+---------------------+
|    ____________     |
|    |/               |
|    |                |
|    |                |
|    |                |
|    |                |
|    |                |
|    |                |
|    |                |
|    |                |
|    |                |
|  __|__              |
+---------------------+""",
#1
"""
+---------------------+
|    ____________     |
|    |/          |    |
|    |           |    |
|    |           |    |
|    |           o    |
|    |                |
|    |                |
|    |                |
|    |                |
|    |                |
|    |                |
|  __|__              |
+---------------------+""",
#2
"""
+---------------------+
|    ____________     |
|    |/          |    |
|    |           |    |
|    |           |    |
|    |           o    |
|    |           |    |
|    |           |    |
|    |                |
|    |                |
|    |                |
|    |                |
|  __|__              |
+---------------------+""",
#3
"""
+---------------------+
|    ____________     |
|    |/          |    |
|    |           |    |
|    |           |    |
|    |           o    |
|    |           |    |
|    |           |    |
|    |          /     |
|    |         /      |
|    |                |
|    |                |
|  __|__              |
+---------------------+""",
#4
"""
+---------------------+
|    ____________     |
|    |/          |    |
|    |           |    |
|    |           |    |
|    |           o    |
|    |           |    |
|    |           |    |
|    |          / \   |
|    |         /   \  |
|    |                |
|    |                |
|  __|__              |
+---------------------+""",
#5
"""
+---------------------+
|    ____________     |
|    |/          |    |
|    |           |    |
|    |           |    |
|    |           o    |
|    |        ---|    |
|    |           |    |
|    |          / \   |
|    |         /   \  |
|    |                |
|    |                |
|  __|__              |
+---------------------+""",
#6
"""
+---------------------+
|    ____________     |
|    |/          |    |
|    |           |    |
|    |           |    |
|    |           o    |
|    |        ---|--- |
|    |           |    |
|    |          / \   |
|    |         /   \  |
|    |                |
|    |                |
|  __|__              |
+---------------------+"""
]
hangmancount=0
wordBank = ['notebook','assignment','facebook', 'childhood','computer']
usedLetters = []
userChoice = ''
rounds = 7
word = random.choice(wordBank)

filler="-"
wordPattern=word[0]+filler*(len(word)-2)+word[-1]

usedLetters.append(word[0])
usedLetters.append(word[-1])
ltrs=[]
print(wordPattern)

while hangmancount < len(hangmanState):
    userChoice = input("Type letter: ").lower()
    if userChoice in usedLetters:
        print("Letter have been already used")
    else:
        usedLetters.append(userChoice)
        print("Used letters: %s" % " ".join(usedLetters))
        ltrs = [l.start() for l in re.finditer(userChoice, word)]
        if len(ltrs) < 1:
            print("HANGMAN %s \n" %hangmanState[hangmancount])
            hangmancount += 1
        else:
            for p in ltrs:
                wordPattern = wordPattern[:p] + userChoice + wordPattern[p+1:]
        print(wordPattern)
        if wordPattern.find(filler) < 0:
            print("You won!")
            break
if hangmancount == len(hangmanState):
    print("You lose!")

