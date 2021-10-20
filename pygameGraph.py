#Preston Yoo
#10-20-21
#Mouse Position
#drawing rect
#moving object
#K_UP up arrow
#K_DOWN down arrow 
#K_RIGHT  left arrow
#K_LEFT   right arrow
import os
import pygame as py

#first thing initiate py
py.init()
#create window
height= 800
width = 900
screen=py.display.set_mode((width, height))
colors = {'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,225), 'purple':(150,0,150), 'white':(255,255,255),'black': (0,0,0),'yellow': (255,211,67),'orange':(255, 165, 0) }
myColor =colors.get('purple')
screen.fill(myColor)
py.display.set_caption("Moving square")
py.display.update()#or flip
#these variables are for the square object
x=width/2
y=height/2 #results in it being nice and even in the screen
wbox=50#height and width of square
hbox=50
#creating our object square
square=py.Rect (x,y,wbox, hbox )
#draw object 
objColor=colors.get('red')
py.draw.rect(screen, objColor, square)
py.display.update()
#create a speed to move the object
speed= 10
run=True
while run:
    py.time.delay(100) #milliseconds 
    for anyThing in py.event.get(): #variable for anytrhing that happneds in pygame to listen to keyboard and mouse
        if anyThing.type ==py.QUIT: #says if Quit is typed something happends
            run =False
    keyPressed= py.key.get_pressed()#records keyboard movement
    if keyPressed[py.K_RIGHT]:
        square.x +=speed #moves square slightly to the right
    if keyPressed[py.K_LEFT]: 
        square.x -=speed #moves square slightly to the left 
    if keyPressed[py.K_UP]: 
        square.y -=speed #moves slightly up
    if keyPressed[py.K_DOWN]: 
        square.y +=speed #moves slightly down 
    if square.x >width-wbox:
        square.x -=width/2
    if square.x == 0:
        square.x +=width/2
    if square.y >height-wbox:
        square.y +=height/2
    if square.y == 0:
        square.y -=height/2
    screen.fill(myColor)
    py.draw.rect(screen, objColor, square)
    py.display.update()
py.quit()