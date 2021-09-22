#Preston Yoo
#9-22-21
#Learning how to use while loops
#While loop: ask player if they want to play (ex: if y is in answer then true, False= if they have f in the answer)
import os, random
os.system('cls')

#Place intructions
name=input("What is your name")
print("Hi,", name)
answer= input("Would you like to play my game")
while ("y" in answer):
    print("guess an number between 1-100")
    randy=random.randgrange (1,100)
    counter=0
    guess=input("please enter an integer")
    while(guess !=randy):
        try:
            guess=int(guess)
            check=True
        except ValueError:
            check= False
            if (True):
                counter+1
                print("Sorry that was not correct please guess again")
                guesss=input("please enter an integer")
            else: 
                print("I am sorry that is not an integer please try again")
                guess=input("please enter an integer")

        #try and except so to convert the guess into interger
        #if check
        #end loop 
    print("Your right! the number was", randy)
    answer=input("Do you want to play again?")
print("thank you for playing come back soon,", name)