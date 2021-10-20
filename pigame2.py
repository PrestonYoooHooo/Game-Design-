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
try: 
    input is 'red' or 'green' or 'blue' or 'purple' or 'white' or 'yellow' or 'orange' or color= color.lower
    check=True
except ValueError:
    check = False
if (check):
    color.lower
else: 
    color= input('sorry please enter a color listed above')
check=True
while check:
    height =input("Enter the height of your window (less then 1200 pixiels and more than 100")
    width =input("Enter the width of your window (less then 1200 pixiels and more than 100")
    try:
        height=int(height)
        width=int(width)
        if height>100 and width>100 and height<1200 and width<1200:
            check=False
        else:
            print("sorry please enter a valid number between 100 and 1200")
            height =input("Enter the height of your window (less then 1200 pixiels and more than 100")
            width =input("Enter the width of your window (less then 1200 pixiels and more than 100")
    except ValueError:
        print("sorry please enter a valid number")

#255 max input and 0 is min
colors = {'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,225), 'purple':(150,0,150), 'white':(255,255,255),'black': (0,0,0),'yellow': (255,211,67),'orange':(255, 165, 0) }
myColor =colors.get()
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