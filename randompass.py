import string
import random


choice_values = string.ascii_letters + string.digits + string.punctuation


passlenght = int( input("enter the length of password you want to generate:"))

password=""

for i in range(passlenght):
    password +=random.choice(choice_values)


print(password)



