import random

target = random.randint(1,100)

count = 0
while True:
    count+=1
    userinput = int( input("enter your number if you want to guess the number: "))

    if(userinput == target):
        print("success: correct guess")
        break
    
    elif(userinput>target):
        print("your number is too large")
    else:
        print("your number is too small")
    

print("you guess in ",count,"attempts")
print("___game over__")

