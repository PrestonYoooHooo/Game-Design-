#Preston Yoo
#9-22-21
#Learning how to use while loops
#While loop: ask player if they want to play (ex: if y is in answer then true, False= if they have f in the answer)

#Place intructions
name=input("What is your name")
print("Hi,", name)
answer= input("Would you like to play my game")
while ("y" in answer):
    print("guess an number between 1-100")
    randy=19
    print(randy)
    counter=0
    guess=input("please enter an integer")
    while(guess !=randy and counter <10) :
        try:
            guess=int(guess)
            check=True
        except ValueError:
            check= False
        if (check):
            if guess==randy :
                print("you're right the number is", randy)
                print("You took", counter, "tries")
                break
            else:
                counter+1
                if (guess>randy):
                    print("try higher")
                else:
                    print("try lower")

                print("sorry that is not the right answer please try again")  
        else: 
            print("I am sorry that is not an integer please try again")
        guess=input("please enter an integer")
        #try and except so to convert the guess into interger
        #if check
        #end loop 
    answer= input("Would you like to play my game again?")
print("thank you for playing come back soon,", name)