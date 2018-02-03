#LOVE calculator.
#Type two  names and compare them.

firstName = list(input("Type first name: "))
secName = list(input("Type second name: "))
vowels = "aeiou"
consonants="qrtpsdfghjklzxcvbnmy"
points = 0

def counting(name, example):
    counter = 0
    for i in range(len(name)):
        if name[i] in example:
            counter += 1
    return counter

while True:
    if firstName[0] == secName[0]:
        points += 20
    if (firstName[0] in vowels) and (secName[0] in vowels):
        points += 10
    if (firstName[0] in consonants) and (secName[0] in consonants):
        points += 5
    if (counting(firstName, vowels) == counting(secName, vowels) ):
        points += 12
    if (counting(firstName, consonants) == counting(secName, consonants)):
        points += 12
    if ((firstName.find('l') > 0) and (secName.find('l') > 0)) \
        or ((firstName.find('o') > 0) and (secName.find('o') > 0)) \
        or ((firstName.find('v') > 0) and (secName.find('v') > 0)) \
        or ((firstName.find('e') > 0) and (secName.find('e') > 0)):
        lovePoints = lovePoints + 7

print("Your love points are %d" %lovePoints)