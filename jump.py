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
lyColor=colors.get('blue')
screen.fill(myColor)
py.display.set_caption("Moving square")
py.display.update()#or flip
#these variables are for the square object
x=width/2
y=height/2 #results in it being nice and even in the screen
wbox=50#height and width of square
hbox=50
boldX=width-300
boldY=height-200
#creating our object square
bolder=py.Rect(boldX,boldY,100,200)
square=py.Rect (x,y,wbox, hbox )
#draw object 
objColor=colors.get('red')
py.draw.rect(screen, objColor, square)
py.display.update()
#create a speed to move the object
run=True
jumpCount=10
jump=False
faspeed=20
while run:
    py.time.delay(100) #milliseconds 
    for anyThing in py.event.get(): #variable for anytrhing that happneds in pygame to listen to keyboard and mouse
        if anyThing.type ==py.QUIT: #says if Quit is typed something happends
            run =False
    keyPressed= py.key.get_pressed()#records keyboard movement
    speedx=10
    speedy=10
    if keyPressed[py.K_RIGHT]:
        if square.colliderect(bolder):
            square.x-=faspeed
        else:
            square.x +=speedx #moves square slightly to the right
    if keyPressed[py.K_LEFT]: 
        if square.colliderect(bolder):
            square.x+=faspeed
        else:
            square.x -=speedx #moves square slightly to the right
    if not jump:
        if keyPressed[py.K_UP]: 
            if py.Rect.collidepoint (square, (boldX,boldY-100)):
                square.y -=faspeed #moves slightly up
            else:
                square.y-=speedy
        if keyPressed[py.K_DOWN]: 
            if square.colliderect(bolder):
                square.y-=speedy
            else:
                square.y +=speedy #moves square slightly to the right
        if keyPressed[py.K_SPACE]:
            jump=True 
    else:
        if jumpCount>=-10:
            square.y-= jumpCount*abs(jumpCount)/2
            jumpCount-=1
            if square.colliderect(bolder):
                square.y=550
                jumpCount=10
                jump=False
        else:
            jumpCount=10
            jump=False
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
    py.draw.rect(screen,lyColor,bolder)
    py.display.update()
py.quit()