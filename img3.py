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
walkRight = [py.image.load('images/Pygame-Tutorials-master/Game/R1.png'), py.image.load('images/Pygame-Tutorials-master/Game/R2.png'), py.image.load('images/Pygame-Tutorials-master/Game/R3.png'), py.image.load('images/Pygame-Tutorials-master/Game/R4.png'), py.image.load('images/Pygame-Tutorials-master/Game/R5.png'), py.image.load('images/Pygame-Tutorials-master/Game/R6.png'), py.image.load('images/Pygame-Tutorials-master/Game/R7.png'), py.image.load('images/Pygame-Tutorials-master/Game/R8.png'), py.image.load('images/Pygame-Tutorials-master/Game/R9.png')]
walkLeft = [py.image.load('images/Pygame-Tutorials-master/Game/L1.png'), py.image.load('images/Pygame-Tutorials-master/Game/L2.png'), py.image.load('images/Pygame-Tutorials-master/Game/L3.png'), py.image.load('images/Pygame-Tutorials-master/Game/L4.png'), py.image.load('images/Pygame-Tutorials-master/Game/L5.png'), py.image.load('images/Pygame-Tutorials-master/Game/L6.png'), py.image.load('images/Pygame-Tutorials-master/Game/L7.png'), py.image.load('images/Pygame-Tutorials-master/Game/L8.png'), py.image.load('images/Pygame-Tutorials-master/Game/L9.png')]
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

py.display.update()
#create a speed to move the object
run=True
bg=py.image.load("images/bgSmaller.jpg")
FIGx=100
FIGy=750
FIG=py.image.load("images/Pygame-Tutorials-master/Game/standing.png")
screen.blit (bg, (0,0))
screen.blit(FIG,(FIGx,FIGy))
py.display.flip#have to use flip for images
jumpCount=10
jump=False
right=False
left=False
walkCount=0
faspeed=20
def redrawGameWindow():
    global walkCount 
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left==True and right==False:  
        screen.blit(walkLeft[walkCount//3], (FIGx,FIGy))
        walkCount += 1                          
    elif right==True and left ==False:
        screen.blit(walkRight[walkCount//3], (FIGx,FIGy))
        walkCount += 1
    else:
        screen.blit(FIG, (FIGx, FIGy))
        walkCount = 0
        
    py.display.update() 
while run:
    py.time.delay(100) #milliseconds 
    for anyThing in py.event.get(): #variable for anytrhing that happneds in py to listen to keyboard and mouse
        if anyThing.type ==py.QUIT: #says if Quit is typed something happends
            run =False
    keyPressed= py.key.get_pressed()#records keyboard movement
    speedx=10
    speedy=10
    if keyPressed[py.K_RIGHT]:
        if FIGx==boldX-50 and FIGy>540:
            FIGx=550
            right=True
            left=False
        else:
            FIGx +=speedx
            right=True
            left=False
    elif keyPressed[py.K_LEFT]: 
        if FIGx==boldX+80 and FIGy>540:
            FIGx=boldX+80
            left=True
            right=False
        else:
            FIGx -=speedx 
            left=True
            right=False
    else:
        left=False
        right=False
        walkCount=0
    if not jump:
        if keyPressed[py.K_SPACE]:
            jump=True 
    else:
        if jumpCount>=-10:
            FIGy-=jumpCount*abs(jumpCount)/1.9
            jumpCount-=1
            if FIGy== boldY-60 and FIGx>boldX-50 and FIGx<boldX+50:
                FIGy=540
                jumpCount=10
                jump=False
        else:
            jumpCount=10
            jump=False
    if FIGy==boldY-60 and FIGx<boldX-50 and FIGx>boldX+50:
        FIGy+=jumpCount*abs(jumpCount)/1.9
        jumpCount=10
    if FIGx==860:
        FIGx=850
    if FIGx==0:
        FIGx=10
    if FIGy==750:
        FIGy=740
    if FIGy==50:
        FIGy=60
    #screen.fill(myColor)
    screen.blit (bg, (0,0))
    py.draw.rect(screen,lyColor,bolder)
    redrawGameWindow()
    py.display.flip()
py.quit()
