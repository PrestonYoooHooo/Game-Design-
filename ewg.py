#Preston Yoo
#9-30-21
import random, os
os.system('cls')
pets=["dog", "cat", "bird", "gerbil"]
fruits=["apple", "pear", "berries", "kiwi",]
name=input("What is your name ")
print("Hi," + name)
answer= input(name + "Would you like to play my game")
answer= (answer).lower ()
while ("y" in answer): #need to add menu in here
    print("Menu")
    print("1 for pets")
    print("2 for fruits")
    answer2=input ("pick 1 or 2 to choose a catagory")
    if answer2 == "2":
        word=random.choice(fruits)
    if answer2 == "1":
        word=random.choice(pets)
    word=(word).lower()
    turns=len(word)+2
    check=True
    guesses=' '
    while (turns>0 and check):
            for letter in word:
                if letter in guesses:
                    print (letter, end=" ")
                    if len(guesses)==len(word):
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
            if check==False:
                print("great job you won with ", turns, "turns left!!!")
    answer=input(name +"do you want to play again?")
print(name + ",Thank you for playing")
