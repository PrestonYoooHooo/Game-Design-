# Preston Yoo
#09/08/2021

#we are going to learn how to assk the user for data and looping

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
line=star 

for lncounter in range(line):
    for counter in range(star):
        print("* ",end=" ")
    print()
    star-=1 #star = star-1
for lncounter in range(line):
    for counter in range(star):
        print("* ", end=" ")

print ("Thank you")