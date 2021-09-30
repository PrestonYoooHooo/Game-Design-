#Preston Yoo
#9-30-21
import random, os
os.system('cls')
Pets=["dog", "cat", "bird", "gerbil"]
name=input("What is your name ")
print("Hi," + name)
answer= input(name + "Would you like to play my game")
while ("y" in answer): #need to add menu in here
    word=random.choice(Pets)
    word=(word).lower()
    turns=len(word)+2
    check=True
    guesses=' '
    while (turns>0 and check):
        for letter in word:
            if letter in guesses:
                print (letter, end=" ")
                if len(guesses)==len(word):
                    if letter in guesses:
                        check=False
            else:
                print("_", end=" ")
        newguess=input ("\n please enter a letter ")
        if newguess in word:
            guesses+=newguess
            print ("good guess")
        else:
            turns -=1 
            print("sorry guess again")
        print ("\n")
    if check:
        print("Sorry best luck next time " )
    else:
        print("great job you won with ", turns, "turns left!!!")
    answer=input(name +"do you want to play again?")
print(name + ",Thank you for playing")
