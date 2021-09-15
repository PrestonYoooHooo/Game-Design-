#Normal Strings
a = "Hello, World!" #you can assign a varibale to one or multiple strings
print(a) # print(a[1]) for a specific part of it
print(a[1])
#len() function returns lenght of the string
a = "Hello, World!"
print(len(a))
# we can print certain parts in it without position
txt = "The best things in life are free!"
print("free" in txt)
#can also do: 
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  #can also do for not:
  txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#Splicing
#By leaving out the start index, the range will start at the first character:
  b = "Hello, World!"
print(b[:5])
#Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])
#Modify
#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
#The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)
#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#formatting
#we cannot combine strings and numbers like this:
age = 36
txt = "My name is John, I am " + age
print(txt) #you can't do this
#But we can combine strings and numbers by using the format() method!
#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#Escape Characters:
#To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash \ followed by the character you want to insert.
#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
#You will get an error if you use double quotes inside a string that is surrounded by double quotes:
txt = "We are the so-called "Vikings" from the north."
#To fix this problem, use the escape character \":
#The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
#Escape Characters
#Other escape characters used in Python:

#Code	Result	Try it
#'	Single Quote	Try it »
#\\	Backslash	Try it »
#\n	New Line	Try it »
#\r	Carriage Return	Try it »
#\t	Tab	Try it »
#\b	Backspace	Try it »
#\f	Form Feed	
#\ooo	Octal value	Try it »
#\xhh	Hex value