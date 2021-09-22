import os, random
os.system('cls')
randy = random.randint(1,20)
print("Hello! Welcome to guess a number!")
for i in range(10):
    userInput=input("guess a number between 1-20")
    try:
        userInput=int(userInput)
        check= True
    except ValueError:
        check= False
    if (check):
        try:
            userInput=randy
            check= True
        except ValueError:
            check=False
            if check: 
                print("congratuations you got the number right please run again if you want to try again!")
                print("You won in ", i+1 ,"tries")
                break
        else:
            print("sorry that wasn't right, guess again!")
    else: 
        print("Sorry please enter a whole number")
print("Thank you for playing")

