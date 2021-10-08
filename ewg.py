#Preston Yoo
#9-30-21
import random, os#allows for random choice
os.system('cls')
pets=["dog", "cat", "bird", "gerbil","goldfish","rock"]
fruits=["apple", "pear", "berries", "kiwi","mango","watermelon",]
shapes=["square", "triangle", "circle", "rectangle","octagon","nonagon",]#Defines the lists and the possible answers
name=input("What is your name ")#to be nice and for scoreboard
print("Hi," + name)
answer= input(name + ",Would you like to play my game")#starts the while y loop
answer= (answer).lower ()#forces it into lowercase
Topscore=0#to have baseline
check=True
def scoreBoard():#create our object file so we can open our scoreboard
    myScore=open('score.txt','r')
    print(myScore.read)()
    myScore.close()
    answer=input("Are you ready to leave?")
while check is True:#this loop is here to prevent the Topscore from reverting back to 0
    while ("y" in answer): #this loop will allow replay ability as long as the user says yes when promopted about playing again
        print("*######################*")
        print("#         Menu         #")
        print("#   1 to guess pets    #")
        print("#   2 to guess fruits  #")
        print("#   3 to guess shapes  #")
        print("# 4 to see scoreboard  #")
        print("#      5 to quit       #")
        print("*######################*")
        answer2=input ("pick 1,2,3,4, or 5 to choose a catagory or to quit the game")#1-3 are catagories and 4 is scoreboard while 5 kills the program
        if answer2 == "5":#breaks loop and nothing is outside so the program ends
            break
        elif answer2 == "4":
            scoreBoard()
            answer=input ("say yes when you want to go back to the menu")
        elif answer2 == "3":#each of these are a random choice command that randomly choses a word from this list
            word=random.choice(shapes)
        elif answer2 == "2":
            word=random.choice(fruits)
        elif answer2 == "1":
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
                score=3*(len(word))+5*turns
                if score>Topscore:
                    score=Topscore
                print("great job you won with", turns, "guesses left!!!Your score was:",score)
        answer=input(name + ",do you want to play again?")
    myFile=open('score.txt', 'a') 
    myFile.write(name + "\t Highest score:\t"+str(Topscore))
    myFile.close() 
    print("your highest score is:",Topscore)
    print(name + ",Thank you for playing")
