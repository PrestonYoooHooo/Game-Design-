import os, random
os.system('cls')

randy = random.randint(1,20)
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
                print("congratuations you got the number right!")
                os.kill
        else:
            print("sorry that wasn't right, guess again!")
    else: 
        print("Sorry please enter a whole number")
