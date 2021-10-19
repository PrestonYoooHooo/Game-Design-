#Preston Yoo
#10-18-21
#starting Pygame
import pygame, os, time
pygame.init()#screen has x and y values, keep in mind when using images and this command initionalizes pygame
#first init then define screen/window/resolution then 
#screen.fill(red) colors the screen red 
#creats a dictionary of colors:
#use usser input to get screen size and color
color= input("what color do you prefer: red, green, blue, purple, white, yellow, orange?")
height = input ("Enter the hight of your window (less then 1500 pixiels)")
try:
    height=int(height)
    height<1501
    check= True
except ValueError:
        check= False
if (check):
        height=int(height)
        height<1501
else: 
    hight=input("Sorry please enter a number")
width = input ("Enter the width of your window (less then 1500 pixiels)")
try:
    width=int(width)
    width<1501
    check= True
except ValueError:
        check= False
if (check):
        sel=int(width)
        height<1501
else: 
    width=input("Sorry please enter a valid number")
colors = {'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,225), 'purple':(150,0,150), 'white':(255,255,255),'black': (0,0,0),'yellow': (255,211,67),'orange':(255, 165, 0) }#255 max input and 0 is min
myColor =colors.get('purple')
screen=pygame.display.set_mode((600,400))#sets width and hight for window and screen is just placeholder name and you can trade numbers for variables and user inputs
red = (255, 0, 0,) #makes window for pygame red change numbers to change tone
purple = (150, 0,150 )#makes purple
pygame.display.set_caption("My Game")
screen.fill(myColor)
pygame.display.update()#updates pygame and your window needed after any change 
run=True#variable for loop to control the game
while run:
    pygame.time.delay(1000) #milliseconds 
    for anyThing in pygame.event.get(): #variable for anytrhing that happneds in pygame to listen to keyboard and mouse
        if anyThing.type ==pygame.QUIT: #says if Quit is typed something happends
            run =False#ends the game
pygame.quit()