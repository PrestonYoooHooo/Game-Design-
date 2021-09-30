#Preston Yoo
#9-24-21
#word guess game
name=input("What is your name")
print("Hi,", name)
answer= input("Would you like to play my game")
while ("y" in answer):
    print("I am thinking of a 7 letter word that starts with p")
    word=("programming")
    counter=1
    guess=input("please enter  7 letter word that starts with p")
    while(guess !=word and counter <10):
                counter=+1
                print("I am sorry that is not the right word")
                guess=input("please enter  7 letter word that starts with p")
    if (counter<10):
                print("your right! The word is", word)
                print("You took", counter, "try/triess")
    else:
        print("sorry you excceded 10 guesses")
    answer= input("Would you like to play my game again?")
print("thank you for playing come back soon,", name)
    

