#Preston Yoo
#9/17/21
# learning about random functions
#intro to Lists(array)

import os, random
os.system('cls')
 
#random generates pseudo-random numbers
for i in range(10):
    randy = random.randint(3,5)
    print(randy)
    randy2= random,random()
    randy2 *=1000
    print (int(randy2))

#arrays in Python are called Lists they use square brakets
fruits=["banna", "apple", "berries", "mango"],"pear" # won't get mango if index is 0-2
print(fruits)
numbers=[1,2,3,4,5,6,]
print(numbers) #with the fruits it will sshow them in quotations due to being characters but it dosen't for numbers because they are numbers
index= random.randint(0,2)
print(fruits[index])
word= random.choice # func. for arrays that allows all options to be chosen without a range
print(word) 
num=random.choice(numbers)
print(num)
