import random

caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lunghezza = int(input("Inserisci il numero di caratteri della password: "))

password = ""

for i in range(lunghezza):
    password += random.choice(caratteri)

print("La tua password generata è:", password)
