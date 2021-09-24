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
            if guess==word:
                print("your right! The word is", word)
                print("You took", counter, "tries")
                break
            else:
                counter=+1
                print("I am sorry that is not the right word")
            guess=input("please enter  7 letter word that starts with p")
    answer= input("Would you like to play my game again?")
print("thank you for playing come back soon,", name)
    

