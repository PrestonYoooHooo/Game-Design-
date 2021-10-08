#Preston Yoo
#10/6/21
#learning how to write a file: 
#write ('w')
#read('r')
#append ('a')
#close()
import os, time
os.system('cls')
#to create a file you must declare a variable name so that we can open the file 
#this is the way to open and create a file 
myFile=open('score.txt','w')
myFile.write ("Hello there, \n My name is Preston \t 1224")
myFile.close()#always close the file as soon as you don't need it anymore
#this is the way to open and read a file
# myFile=open('score.txt','r')
# print(myFile.read)()
# myFile.close
#write things on file
anotherFile=open('score.txt', 'w') #same file diff. variable
anotherFile.write("I sorry changed my mind")#writes over what wass previously written use append if you want to save previous data
anotherFile.close
#reprint
# myFile=open('score.txt','r')
# print(myFile.read)()
# myFile.close
#append
anotherFile=open('score.txt', 'a')
anotherFile.write("Let'ss try again \n The score is \t 23")
anotherFile.close()
myFile=open('score.txt','r')
print(myFile.readline())#printss first line
print(myFile.readline())#prints file one line at a time if you repeat
myFile.close


