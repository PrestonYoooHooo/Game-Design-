import pygame
pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('images/Pygame-Tutorials-master/Game/R1.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R2.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R3.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R4.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R5.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R6.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R7.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R8.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/R9.png')]
walkLeft = [pygame.image.load('images/Pygame-Tutorials-master/Game/L1.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L2.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L3.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L4.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L5.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L6.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L7.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L8.png'), pygame.image.load('images/Pygame-Tutorials-master/Game/L9.png')]
bg = pygame.image.load('images/Pygame-Tutorials-master/Game/bg.jpg')
char = pygame.image.load('images/Pygame-Tutorials-master/Game/standing.png')
widthd=900
heightd=800
xi=widthd/2
yi=heightd/2 #results in it being nice and even in the screen
wbox=50#height and width of square
hbox=50
boldX=500-400
boldY=480-280
#creating our object square
bolder=pygame.Rect(boldX,boldY,100,200)
square=pygame.Rect (xi,yi,wbox, hbox )
colors = {'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,225), 'purple':(150,0,150), 'white':(255,255,255),'black': (0,0,0),'yellow': (255,211,67),'orange':(255, 165, 0) }
x = 50
y = 400
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10
bolder=pygame.Rect(boldX,boldY,100,200)
objColor=colors.get('red')
left = False
right = False
walkCount = 0
bg=pygame.image.load("images/bgSmaller.jpg")
FIGx=300
FIGy=300
FIG=pygame.image.load("images/Pygame-Tutorials-master/Game/standing.png")
win.blit (bg, (0,0))
win.blit(FIG,(FIGx,FIGy))

def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update() 
    


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False
    if x ==boldX-50 and y>540:
        x -= vel*2
        left = True
        right = False
    if x ==boldX+50 and y>540:
        x=boldX+80
        left=False
        right=True
    if y== boldY-60 and x>boldX-50 and x<boldX+50:
        FIGy=540
        jumpCount=10
        jump=False


    redrawGameWindow() 
    pygame.draw.rect(win,objColor,bolder)
    
    
pygame.quit()