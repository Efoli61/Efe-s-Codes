import random

length = int(input('What will be the length for the password? '))
chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = ""

for i in range(length):
    password += random.choice(chars)

print("Generated Password:", password)

