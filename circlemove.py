#Preston Yoo
#10-20-21
#Mouse Position
#drawing rect
#moving object
#K_UP up arrow
#K_DOWN down arrow 
#K_RIGHT  left arrow
#K_LEFT   right arrow
#and circle creation and movements 
import os
import pygame as py
import random

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
#these variables are for the square object and circle
xi=random.randint(10,900)
yi=random.randint(10,800)
xi=int(xi)
yi=int(yi)
lives=10
x=width/2
y=height/2 #results in it being nice and even in the screen
wbox=50#height and width of square
hbox=50
withe=0
#creating our object square
square=py.Rect (x,y,wbox,wbox,)
cirrai=wbox/2
cirrai=int(cirrai)
#draw object 
objColor=colors.get('red')
boiColor=colors.get('yellow')
py.draw.rect(screen, objColor, square)
py.draw.circle(screen,boiColor,(xi,yi),cirrai,withe)
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
    if keyPressed[py.K_a]:
        xi -=speed #moves square slightly to the right
    if keyPressed[py.K_d]: 
        xi +=speed #moves square slightly to the left 
    if keyPressed[py.K_w]: 
        yi -=speed #moves slightly up
    if keyPressed[py.K_s]: 
        yi +=speed #moves slightly down 
    if py.Rect.collidepoint(square,(xi,yi)):
        cirrai+=wbox/2
        square.x=random.randint(10,width)
        square.y=random.randint(10,height)
        lives-1
    if square.x >900: 
        square.x=0
    if square.x<0:
        square.x=900
    if square.y >800:
        square.y=0
    if square.y <0:
        square.y = 800
    if xi>900-cirrai:
        xi-=speed*2
    if xi<0+cirrai:
        xi+=speed*2
    if yi>800-cirrai:
        yi-=speed*2
    if yi<0+cirrai:
        yi+=speed*2
    if cirrai>120:
        print("Circle has won!")
        run =False
    point=(xi,yi)
    screen.fill(myColor)
    py.draw.rect(screen, objColor, square)
    py.draw.circle(screen,boiColor, (xi,yi),cirrai,withe)
    py.display.update()
py.quit()