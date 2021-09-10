# Preston Yoo
#09/08/2021,#09/10/2021
#Libraries
import os
#we are going to learn how to assk the user for data and looping
os.system ('cls')
star= int(input("please enter number of stars")) #allow to get values from the user
#print ("* * * *")
# loop
# type cast means to force a change of data
#variable to count lines
#the star = star-1  or star -=1 removes one star from the row per loop typing 4 and:
# *  *  *  *  
# *  *  *  
# *  *  
#*  
#if you want to reverse it print spaces before they begin
line=star 
space=line-star
for lncounter in range(line):
    for counter in range(star):
        print("* ",end=" ")
    for counter in range(space):
        print("  ", end=" ")
    for counter in range(star):
        print("* ",end=" ")
    print()#print like this to create a new line
    star-=1 #star = star-1
    space+=2
print(" ",end=" ")
print("Thank you")