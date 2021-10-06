#Preston Yoo
#9-30-21
#same as ewg but scoreoard date and using text file to store information

import random, os
os.system('cls')
pets=["dog", "cat", "bird", "gerbil"]
fruits=["apple", "pear", "berries", "kiwi",]
shapes=["square", "triangle", "circle", "rectangle",]
name=input("What is your name ")
print("Hi," + name)
answer= input(name + ",Would you like to play my game")
answer= (answer).lower ()
while ("y" in answer): #need to add menu in here
    print("*######################*")
    print("#         Menu         #")
    print("#      1 for pets      #")
    print("#     2 for fruits     #")
    print("#     3 for shapes     #")
    print("#      4 to quit       #")
    print("*######################*")
    answer2=input ("pick 1,2,3, or 4 to choose a catagory or to quit the game")
    if answer2 == "4":
        break
    if answer2 == "3":
        word=random.choice(shapes)
    if answer2 == "2":
        word=random.choice(fruits)
    if answer2 == "1":
        word=random.choice(pets)
    word=(word).lower()
    turns=len(word)+2
    check=True
    guesses=' '
    
    while (turns>0 and check):
        guessLen=0
        for letter in word:
            if letter in guesses:
                print (letter, end=" ")
                guessLen= guessLen+1
            else:
                print("_", end=" ")
        print (guessLen)
        if guessLen==len(word):
            check=False
        if check:
            newguess=input ("\n please enter a letter")
            if newguess in word:
                guesses+=newguess
                print ("good guess")
            else:
                turns -=1 
                print("sorry guess again")
            print ("\n")
        else:
            # guesses+=newguess
            print("great job you won with", turns, "guesses left!!!")
    answer=input(name + ",do you want to play again?")
print(name + ",Thank you for playing")
