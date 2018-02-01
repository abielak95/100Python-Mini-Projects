#Encrypt / Decrypt Algorithm

encryptTab = "aeiou"
decryptTab = "12345"

while True:
    userMode = int(input("Type 1 to encrypt a sentence, 2 to decrypt a sentence, 3 to exit: "))
    if userMode == 1:
        stringToEncrypt = str(input("Type a sentence to encrypt: ")).lower()
        transTab = str.maketrans(encryptTab, decryptTab)
        print(stringToEncrypt.translate(transTab))
    elif userMode == 2:
        stringToDecrypt = str(input("Type a sentence to decrypt: ")).lower()
        transTab = str.maketrans((decryptTab, encryptTab))
        print(stringToDecrypt.translate(transTab))
    elif userMode == 3:
        break
    else:
        print("Wrong input!")
