name=input("What is your name")
print("Hi,", name)
answer= input("Would you like to play my game")
while ("y" in answer):
    word=("cat")
    for letter in word:
        print("_ ", end= " ")
    print ("\n")
    guess=input("guess the letters of the 3 letter word starting with the first in 10 guess or less!. Hint: its a pet!")
    firstl=(word[0])
    counter=1
    #can base counter limit on word ex: counter 5=len(word)2 and add more limit accordingly also create variable for <counter
    #also can uses turns and subtract when incorrect in guess
    while(guess !=firstl and counter <10):
        counter=+1
        print("I am sorry that is not the right letter")
        guess=input("try again")
        if (counter<10):
            print("your right! The letter is", firstl)
            for letter in word:
                print(word[0], "_", "_", end= " ")
                guess2=input("guess the second letter of the word")
                sec2=(word[1])
                while(guess2 !=sec2 and counter <10):
                    counter=+1
                    print("I am sorry that is not the right letter")
                    guess2=input("try again")
                if (counter<10):
                    print("your right! The letter is", sec2)
                    for letter in word:
                        print(word[0], word[1], "_", end=" ")
                        guess3=input("guess the final letter of the word")
                        guess=(guess)
                        third3=(word[2])
                        while(guess3 !=third3 and counter<10):
                            counter=+1
                            print("I am sorry that is not the right letter")
                            third3=input("try again")
                        if counter<10:
                            print ("Your right! the final letter is", third3, "and the word is cat!")
                            print("You took", counter, "try/ies to get the word")
                            break
                        else:
                            print("sorry you excceded 10 gueses")
                        break
                    break
                else:
                    print("sorry you excceded 10 gueses")  
                break    
        else:
            print("sorry you excceded 10 guesses")
    answer= input("Would you like to play again?")
print("Thank you for playing",name, "!!!")
