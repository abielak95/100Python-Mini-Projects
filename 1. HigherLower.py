import random

number = random.randint(0, 100)
input_var = int(input("Enter some data: "))
z=0

while(z<10):
    if input_var == number:
        print("Excellent!")
        break

    elif input_var < number:
        input_var = int(input("Type greater number: "))

    elif input_var > number:
        input_var = int(input("Type lover number: "))

    z+=1