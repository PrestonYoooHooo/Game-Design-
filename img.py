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
win = py.display.set_mode((900,800))
#first thing initiate py
py.init()
#create window
height= 800
width = 900
x=50 
y=400 
right=False
left=True
walkCount=0
walkLeft={py.image.load('images/Pygame-Tutorials-master/Game/L1.png'), py.image.load('images/Pygame-Tutorials-master/Game/L2.png'), py.image.load('images/Pygame-Tutorials-master/Game/L3.png'),py.image.load('images/Pygame-Tutorials-master/Game/L4.png'), py.image.load('images/Pygame-Tutorials-master/Game/L5.png'), py.image.load('images/Pygame-Tutorials-master/Game/L6.png'), py.image.load('images/Pygame-Tutorials-master/Game/L7.png'), py.image.load('images/Pygame-Tutorials-master/Game/L8.png'), py.image.load('images/Pygame-Tutorials-master/Game/L9.png')}
walkRight={py.image.load('images/Pygame-Tutorials-master/Game/R1.png'),py.image.load('images/Pygame-Tutorials-master/Game/R2.png'), py.image.load('images/Pygame-Tutorials-master/Game/R3.png'),py.image.load('images/Pygame-Tutorials-master/Game/R4.png'),py.image.load('images/Pygame-Tutorials-master/Game/R5.png'),py.image.load('images/Pygame-Tutorials-master/Game/R6.png'),py.image.load('images/Pygame-Tutorials-master/Game/R7.png'),py.image.load('images/Pygame-Tutorials-master/Game/R8.png'),py.image.load('images/Pygame-Tutorials-master/Game/R9.png')}
def redrawGameWindow():
    global walkCount
    if walkCount + 1 >= 27:
            walkCount = 0
            win.blit(bg, (0,0))
    if left:  
            win.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1                          
    elif right:
            win.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
    else:
            win.blit(standing, (x, y))
            walkCount = 0
screen=py.display.set_mode((width, height))
colors = {'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,225), 'purple':(150,0,150), 'white':(255,255,255),'black': (0,0,0),'yellow': (255,211,67),'orange':(255, 165, 0) }
standing= py.image.load('images/Pygame-Tutorials-master/Game/standing.png')
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

py.display.update()
#create a speed to move the object
run=True
bg=py.image.load("images/bgSmaller.jpg")
FIGx=300
FIGy=300
FIG=py.image.load("images/Pygame-Tutorials-master/Game/standing.png")
screen.blit (bg, (0,0))
screen.blit(FIG,(FIGx,FIGy))
py.display.flip#have to use flip for images
jumpCount=10
jump=False
faspeed=20
def redrawGameWindow():
    # We have 9 images for our walking animation, I want to show the same image for 3 frames
    # so I use the number 27 as an upper bound for walkCount because 27 / 3 = 9. 9 images shown
    # 3 times each animation.
    global walkCount
    
    win.blit(bg, (0,0))  

    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  # If we are facing left
        win.blit(walkLeft[walkCount//3], (x,y))  # We integer divide walkCounr by 3 to ensure each
        walkCount += 1                           # image is shown 3 times every animation
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(FIG, (x, y))
while run:
    py.time.delay(100) #milliseconds 
    for anyThing in py.event.get(): #variable for anytrhing that happneds in pygame to listen to keyboard and mouse
        if anyThing.type ==py.QUIT: #says if Quit is typed something happends
            run =False
    keyPressed= py.key.get_pressed()#records keyboard movement
    speedx=10
    speedy=10
    if keyPressed[py.K_RIGHT]:
        if FIGx==boldX-50 and FIGy>540:
            FIGx=550
            left = True
            right = False
        else: 
            left = False
            right = True
            FIGx+=speedx
            walkCount = 0 
    if keyPressed[py.K_LEFT]: 
        if FIGx==boldX+80 and FIGy>540:
            FIGx=boldX+80
            left=False
            right=True
        else:
            left =True
            right=False
            FIGx -=speedx #moves square slightly to the right
    if left==False and right==False:
        left = False
        right = False
        walkCount = 0
    if not jump:
        if keyPressed[py.K_UP]: 
            if FIGy == boldY+100 and FIGx >450 and FIGx<550:
                FIGy=540 #moves slightly up
            else:
                FIGy-=speedy
        if keyPressed[py.K_DOWN]: 
            if FIGy == boldY-60 and FIGx>boldX-50 and FIGx<boldX+50:
                FIGy=540
            else:
                FIGy +=speedy #moves square slightly to the right
        if keyPressed[py.K_SPACE]:
            jump=True 
    else:
        if jumpCount>=-10:
            FIGy-=jumpCount*abs(jumpCount)/2
            jumpCount-=1
            if FIGy== boldY-60 and FIGx>boldX-50 and FIGx<boldX+50:
                FIGy=540
                jumpCount=10
                jump=False
        else:
            jumpCount=10
            jump=False
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
    screen.blit(FIG,(FIGx,FIGy))
    redrawGameWindow
    py.draw.rect(screen,lyColor,bolder)
    py.display.flip()
py.quit()