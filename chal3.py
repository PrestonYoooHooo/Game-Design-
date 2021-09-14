import os

os.system("cls")

ine= 20
flo= 6.5
print(type(ine))
print(type(flo))
num1=24
userInput=input("Type an integer")
try:
    print(type(userInput)) 
    userInput=int(userInput)
    check=True      
except ValueError:
    check = False
if (check):
    if userInput>0:
        print(num1+userInput-userInput*userInput/userInput)
        print(num1%userInput)
    else:
        print("Sorry enter a non-zero number")

else:
    print("Sorry I can't add that number")
