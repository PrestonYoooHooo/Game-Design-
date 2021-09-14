# Preston Yoo
# Date: 09/14/2021
# Data type and how to check for the right type

import os
os.system('cls')

#variable declare and initialize
num = 30
#int= 1 integer, float= 0.5 decimal, char= 'a' a chacter, string= ("hello") sting of chacters 
#these are primitive data types
print(type(num)) #shows that num is an integer
num=6.7
print(type(num)) #shows it is a float (a decimal)
#shows both
userInput=input("Type Something")
print(type(userInput)) #dosen't automatically show float if decimal 
userInput=float(userInput) #worked after classsifying it but if you don't put num it won't work
#How to check for your data
userInput=input("Type Something")
try:
    print(type(userInput)) 
    userInput=float(userInput)
    check=True      #boolean (binary/ True or False)
except ValueError:
    check = False
#using conditional statement if/else
if (check):
    print(num+userInput)
else:
    print("Sorry I can't add that number")

print(num/0) #can't do that sso ask for 
