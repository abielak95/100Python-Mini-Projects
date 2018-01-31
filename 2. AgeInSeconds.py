#Compute your age in seconds

import datetime
userBirthDate=''

while True:
    userBirthDate = input("Input your date of birht in YYYY-MM-DD format: ")
    try:
        birthDate = datetime.datetime.strptime(userBirthDate, '%Y-%m-%d')
        difference = (datetime.datetime.now() - birthDate).total_seconds()

        print("Your life in seconds: %d" % difference)
    except:
        print("Incorrect date format!")

