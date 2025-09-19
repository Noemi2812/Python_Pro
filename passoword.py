import random
elementi = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lunghezza = int(input("Quanto deve essere lunga la password?"))

passaword = ""
for i in range(lunghezza):

    passaword = passaword + random.choice(elementi)
    

print(passaword)
