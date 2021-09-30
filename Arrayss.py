#Learning Python Collectionss

#Preston Yoo
#9/28/21
#this is where I would import random if it worked
#Lists
names= ["Alex", "Jack", "Mary", "Ellen", "Josh"]
print(names[2])
print(names)
for nam in names:
    print(nam, end=" ")
print("/n These are all the names ")

print(names[-1])#goes backwards on list as long as yitss not bigger than index
print(names [2:5])#prints Mary to Josh
#range of indexes
names[3]="Betty" #Changes name in 3 pos in this case ellen
if "Ellen" in names:
    print ("you win")
else:
    print("sorry your wrong")
#length of arraay
print(len(names))
#add elements using apppend()
names.append("Owen")#adds Owen to end of list
names.insert(4, "Joan")#adds name to index 4
#copy a list to another list
otherNames= names.copy()#copies whole list
print(otherNames)
otherNames= names[2:6].copy()#copy parts of list
compParts=["keyboard", "printer", "MotherBoard", "CPU", "cooling fan", "storage"]
word=("CPU").lower
guess=input("guess the word I am thinking")
while(guess not in word):
    guess=(guess).lower
    if guess in word:
        print("You are right!!")
        break
    else: 
        print("wrong")
        guess=input("try again")
print("thank you for playing")

