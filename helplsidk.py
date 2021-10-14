
#Word Game
#Preston Yoo
#09/29/2021
# We are creating a list of words
# randomly select a word from the list for the user to guess
# give the user some turns
# show the word to the user with the characters guessed  
# play as long as the user has turns or has guessed the word

import random, os
os.system('cls')
#function to update dashes and letters
def updateWord(word, guesses, letCount):#function for the word count and guess and showing the letters left to guess
    for letter in word:
        if letter in guesses:
            print(letter,end=" ")
            letCount+=1\

        else:
            print('_', end=' ')
    return letCount
#define function for Menu
def scoreBoard():#function for scoreboard to be read and then open menu again
    print("Scoreboard:")
    myScore=open('score.txt','r')
    print(myScore.read)()
    myScore.close()
    answer2=input("Are you ready to return to the menu?")
    if 'y' in answer2:
        Menu() #fun sends back to menu
def Exitnow():#function for ending the game and updating the player's highest score to the file
    myFile=open('score.txt', 'a') 
    myFile.write(name + "\t Highest score:\t"+str(maxScore))
    myFile.close() 
    print("Thank you for playing") 
    os._exit 
def Menu():#function to bring player back to menu and start a new game
    print("Guess the word in a certian amont of guesses to win!")
    print("Guess a long word in the fewest guesses to get the most points!")
    print("########################################")
    print("#                MENU                  #")
    print("#                                      #")
    print("#       1. Animals                     #")
    print("#       2. Computer PArts              #")
    print("#       3. Fruits                      #")
    print("#       4. ScoreBoard                  #")
    print("#       5. Exit                        #")
    print("#    To play the game select 1-4       #")
    print("#       To exit select 5               #")
    print("########################################")
    print()
    sel=input("What would you like to do? ")
    # add the Try and except before you force sel to be an int
    try:
        sel=int(sel)
        check= True
    except ValueError:
        check= False
    if (check):
        sel=int(sel)
    else: 
        sel=input("Sorry please enter an integer")
    try: #makes sure the integer is in acceptable range
        sel<6 and sel<0
        check= True 
    except ValueError:
        check=False
    if (check):
        sel<6 and sel>0
    else: 
        sel=input("Sorry please enter an integer between 1-5")
    if sel==5:
        Exitnow()
    elif sel ==4:#create command to return to menu
        scoreBoard()
    return sel
def selWord(sel):#function for chosing which list to randomly choose the word from
    if sel == 1:
        word= random.choice(animals)
    elif sel ==2:
        word= random.choice(compParts)
    elif sel ==3: 
        word= random.choice(fruits)
    
    return word
# create the function for the score board and comeback to main menu
animals=["tiger", "elephant","bear","parrot","panther","humans"]
fruits=["banana", "strawberries","kiwi","dragonfruit","durian","watermelon"]
compParts=["keyboard", "Monitors", "computer","trackpad", "case","Operating System"]
name= input("What is your name? ")
maxScore=0 #to store highest Score
sel = Menu()
print(sel)
while sel==1 or sel==2 or sel==3:
    print(name, " Good Luck! you have 5 chances to guess")
    word= selWord(sel)
    word = word.lower()
    wordCount=len(word)
    turns= wordCount+2  #depending on the lenght if the word
    letCount=0 #variable to check if the user guessed the word
    guesses=''
    score=0#to store the score every game
    letCount=updateWord(word, guesses, letCount)
    while turns > 0 and letCount<wordCount:
        print()
        newguess=input (name + " Give me a letter ")
        newguess= newguess.lower()
        if newguess in word:
            guesses += newguess#adds the letter to the letters already there
            
            print("you guessed one letter ")
        else:
            turns -=1
            print("Sorry, you have ", turns, "turns left")
        letCount=0
        letCount= updateWord(word, guesses, letCount)
    os.system('cls')
    score=3*wordCount+5*turns
    if score > maxScore:
        maxScore=score
    print(maxScore)
    sel=Menu()