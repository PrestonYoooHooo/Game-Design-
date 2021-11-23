#Preston Yoo
#10-28-21
#window ssettings for a game

import pygame, os,random,time

os.system('cls')
pygame.init()
#list fot menu Messages
gameMessages= ["Play Game","Settings","Instructions","Scoreboard","Exit"]
settingMessages=["Screen Size","Background Colors", "Object Colors", "Sounds On/Off","Back"]#can use same logic for main menu
sizeMessages=["700*700", "800*800", "900*900", "1000*1000","Back"]
BacoMessages=["Red","Blue","White","Orange","Back"]
CoMessages=['Orange','Red','White','Blue','Back']
ScMessages=['Score 1','Score 2','Score 3', 'Score 4', 'Back']
InMessages= ['Get a friend', 'Gather 3 flags before them', 'Push them back with your laser', 'Enjoy your ruined friendship', 'Back']
PlMessages= ['Level 1', 'Level 2', 'Back']
walkRight = [pygame.image.load('images/Right Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 2.jpeg'),pygame.image.load('images/Right Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 3.jpeg'),pygame.image.load('images/Right Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 4.jpeg'),pygame.image.load('images/Right Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 5.jpeg'),pygame.image.load('images/Right Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 6.jpeg'),pygame.image.load('images/Right Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 7.jpeg'), pygame.image.load('images/Right Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 8.jpeg'),pygame.image.load('images/Right Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 9.jpeg'),pygame.image.load('images/Right Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png.jpeg')]
walkLeft = [pygame.image.load('images/Left Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 2.jpeg'),pygame.image.load('images/Left Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 3.jpeg'),pygame.image.load('images/Left Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 4.jpeg'), pygame.image.load('images/Left Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 5.jpeg'), pygame.image.load('images/Left Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 6.jpeg'),pygame.image.load('images/Left Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 7.jpeg'),pygame.image.load('images/Left Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 8.jpeg'), pygame.image.load('images/Left Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png copy 5.jpeg'), pygame.image.load('images/Left Mov./716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png copy 6.jpeg')]
StL = [pygame.image.load('images/716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 2.jpeg')]
StR = [pygame.image.load('images/716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png.jpeg')]
sebg = [pygame.image.load('images/images copy.jpg')]
eibg = [pygame.image.load('images/images copy 2.jpg')]
nibg = [pygame.image.load('images/images copy 3.jpg')]
tebg = [pygame.image.load('images/images.jpg')]
sebg2 = [pygame.image.load('images/lava-lake-active-valcano-rj-2560x1700.jpg')]
eibg2 = [pygame.image.load('images/lava-lake-active-valcano-rj-2560x1700 copy.jpg')]
nibg2 = [pygame.image.load('images/lava-lake-active-valcano-rj-2560x1700 copy 2.jpg')]
tebg2 = [pygame.image.load('images/lava-lake-active-valcano-rj-2560x1700 copy 3.jpg')]
lamon = [pygame.image.load('images/95-957201_lava-muk-pokemon-lava.jpg')]
p1 = [pygame.image.load('images/pngtree-battle-player-1-vs-2-logo-versus-png-image_2899070.jpeg')]
p2 = [pygame.image.load('images/pngtree-battle-player-1-vs-2-logo-versus-png-image_2899070.jpeg')]
fl = [pygame.image.load('images/Unknown.png')]#I define/load all of my picture variables 
#global variables: they work anywhere in the program
colors = {'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,225), 'purple':(150,0,150), 'white':(255,255,255),'black': (0,0,0),'yellow': (255,211,67),'orange':(255, 165, 0), 'black': (0,0,0)}
WHITE=colors.get('white')
BLACK=colors.get('black')
ORANGE=colors.get('orange')
RED=colors.get('red')
PURPLE=colors.get('purple')
BLUE=colors.get('blue')
WIDTH=800
HEIGHT=800
wbox=25
hbox=30
x=70
y=150
boldx1=200
boldy1=200
boldx2=WIDTH-200
boldy2=200
boldy3=HEIGHT-200
boldx3=200
boldx4=WIDTH-200
boldy4=HEIGHT-200
bolder1=pygame.Rect(boldx1,boldy1,75,75)
bolder2=pygame.Rect(boldx2,boldy2,75,75)
bolder3=pygame.Rect(boldx3,boldy3,75,75)
bolder4=pygame.Rect(boldx4,boldy4,75,75)# the cords for the wall that change depending on the height of the screen 
newgame1=False
newgame2=False
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Setting Window')
square=pygame.Rect(x,y,wbox,hbox)
#Declare FONTS
TITLE_FONT=pygame.font.SysFont('comicsans',80)
SubTitle=pygame.font.SysFont('comicsans', 40, italic=True)
MENU_FONT=pygame.font.SysFont('comicsans',40)
INSTUR_FONT=pygame.font.SysFont('comicsans',30)
text=TITLE_FONT.render('message',1,BLACK)
counter=0
walkCount1= 0
walkCount2= 0
left=False
right=False
hitstun=False 
lastr1= False
lastl1= False 
lastr2= False
lastl2= False#used to determine the last dircetion each of them faced 
FIGx1=50
FIGy1=HEIGHT-50
FIGx2=WIDTH-50
FIGy2= HEIGHT-50#they start at oppisted sides of the screen 
def redrawGameWindowforp1():
    global walkCount1 
    if walkCount1 + 1 >= 27:
        walkCount = 0
        
    if left==True and right==False:  #for every time they take a step the walkcount is moved up by one and their image is changed constanly to make it look like they are moving in a certian direction
        win.blit(walkLeft[walkCount//3], (FIGx1,FIGy1))
        walkCount += 1                          
    elif right==True and left ==False:
        win.blit(walkRight[walkCount//3], (FIGx1,FIGy1))
        walkCount += 1
    elif lastr1== True and lastl1 == False:
        win.blit(StR, (FIGx1, FIGy1))
        walkCount = 0
    else:
        win.blit(StL,FIGx1,FIGy1)
        walkCount=0
def redrawGameWindowforp2():
    global walkCount1 
    if walkCount1 + 1 >= 27:
        walkCount = 0
        
    if left==True and right==False:  
        win.blit(walkLeft[walkCount//3], (FIGx2,FIGy2))
        walkCount += 1                          
    elif right==True and left ==False:
        win.blit(walkRight[walkCount//3], (FIGx2,FIGy2))
        walkCount += 1
    elif lastr2== True and lastl2 == False:
        win.blit(StR, (FIGx2, FIGy2))
        walkCount = 0
    else:
        win.blit(StL,FIGx2,FIGy2)
        walkCount=0
def create_NewWindow(winTitile):
    pygame.display.set_caption(winTitile)
    win.fill(WHITE)
    pygame.display.update()
def display_Title(message,y):#that comes with def
    win.fill(WHITE)
    pygame.time.delay(100)
    text=TITLE_FONT.render(message,1,BLACK)#message now variable
    xm=WIDTH/2-text.get_width()/2
    ym=40
    win.blit(text,(xm,ym))
    pygame.display.update()
    pygame.time.delay(100)
    

def Menu_function(Messages,y):
    pygame.time.delay(100)
    square.y=y
    xy=15
    ym=y-xy
    #this works because the other xm is in another function sso it is sepaerate aka a local variable
    xm=x+wbox+10

    for i in range (0,len(Messages)):
        word=Messages[i]
        pygame.draw.rect(win, ORANGE,square)
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm,ym))
        pygame.display.update()
        pygame.time.delay(100)
        ym+=100
        square.y=ym+15
    
display_Title("TestyGame",y)
Menu_function(gameMessages,150)
run=True
play=True
while run:
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            run=False
        if eve.type ==pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses [0]:
                mouse_pos =pygame.mouse.get_pos()
                print (mouse_pos)
                xp=mouse_pos[0]
                yp=mouse_pos[1]
                print (x,y)
                #if py.Rect.collidepoint(square,(mouse_pos)):
                if xp >x and xp<x+wbox and yp>y and yp<245 and counter is 0:
                    xp=0#this resets the mouse postion so double pressing dossen't occur
                    yp=0
                    win.fill(WHITE)#it says white but it will change to any background color you chose
                    create_NewWindow("Play Game")
                    display_Title("Play Game",40)
                    Menu_function(PlMessages,150)
                    counter+=7
                    pygame.time.delay(100)
                if xp>x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 0:# the counter system allows us to see where we are and along with mouse postion allows for smooth and clean transitions between screens
                    pygame.event.clear(pygame.MOUSEBUTTONDOWN)
                    xp=0
                    yp=0
                    win.fill(WHITE)
                    create_NewWindow("Settings")
                    display_Title("Settings",40)
                    Menu_function(settingMessages,150)
                    counter+=1
                if xp>x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 0:
                    xp=0
                    yp=0
                    win.fill(WHITE)
                    create_NewWindow("Instructions")
                    display_Title("Instructions",40)
                    Menu_function(InMessages,150)
                    pygame.time.delay(100)
                    counter+=5
            #myFile=open ('insturctions.txt','r')
            #yi=150
            #for line in myFile.readlines():
                #text=INSTRUCTIONS_FONT.render(line, 1, BLACK)
                #win.blit(text,(40,yi))
                #pygame.display.update
                #pygame.time.delay(100)
               # yi+=50
            #myFile=close

                if xp>x and xp<x+wbox and yp>y and yp<545 and yp>445 and counter is 0:
                    xp=0
                    yp=0                  
                    win.fill(WHITE)
                    create_NewWindow("Score Board")
                    display_Title("Score Board",40)
                    Menu_function(ScMessages,150)
                    pygame.time.delay(100)
                    counter+=6
                if xp>x and xp<x+wbox and yp>y and yp<645 and yp>545 and counter is 0:
                    run=False
                if xp>x and xp<x+wbox and yp>y and yp<245 and counter is 1:
                    xp=0
                    yp=0                  
                    win.fill(WHITE)
                    create_NewWindow("Screen Size")
                    display_Title("Screen Size",40)
                    Menu_function(sizeMessages,150)
                    counter+=1
                if xp>x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 1:
                    xp=0
                    yp=0                 
                    win.fill(WHITE)
                    create_NewWindow("Background Color")
                    display_Title("Background Color",40)
                    Menu_function(BacoMessages,150)
                    counter+=2
                    pygame.time.delay(100)
                if xp>x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 1:
                    xp=0
                    yp=0                 
                    win.fill(WHITE)
                    create_NewWindow("Object Color")
                    display_Title("Object Color",40)
                    Menu_function(CoMessages,150)
                    counter+=3
                    pygame.time.delay(100)
                if xp>x and xp<x+wbox and yp>y and yp<545 and yp>345 and counter is 1:
                    xp=0
                    yp=0                 
                if xp>x and xp<x+wbox and yp>y and yp<645 and yp>545 and counter is 1:
                    xp=0
                    yp=0
                    win.fill(WHITE)
                    display_Title("TestyGame",y)
                    Menu_function(gameMessages,150)
                    counter-=1
                if xp >x and xp<x+wbox and yp>y and yp<245 and counter is 2:
                    xp=0
                    yp=0
                    HEIGHT=700#sets height
                    WIDTH=700
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    create_NewWindow("Screen Size")
                    display_Title("Screen Size",40)
                    Menu_function(sizeMessages,150)
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 2:
                    xp=0
                    yp=0
                    HEIGHT=800
                    WIDTH=800
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    create_NewWindow("Screen Size")
                    display_Title("Screen Size",40)
                    Menu_function(sizeMessages,150)
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 2:
                    xp=0
                    yp=0                  
                    HEIGHT=900
                    WIDTH=900
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    create_NewWindow("Screen Size")
                    display_Title("Screen Size",40)
                    Menu_function(sizeMessages,150)
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<545 and yp>445 and counter is 2:
                    xp=0
                    yp=0
                    HEIGHT=1000
                    WIDTH=1000
                    win=pygame.display.set_mode((WIDTH,HEIGHT))
                    create_NewWindow("Screen Size")
                    display_Title("Screen Size",40)
                    Menu_function(sizeMessages,150)
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<645 and yp>545 and counter is 2:
                    xp=0
                    yp=0                    
                    win.fill(WHITE)
                    display_Title("Settings",y)
                    Menu_function(settingMessages,150)
                    counter-=1
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<245 and counter is 3:
                    xp=0
                    yp=0  
                    WHITE=colors.get('red')                
                    win.fill(WHITE)
                    create_NewWindow("Background Color")
                    display_Title("Background Color",40)
                    Menu_function(BacoMessages,150)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 3:
                    xp=0
                    yp=0  
                    WHITE=colors.get('blue')             
                    win.fill(WHITE)
                    create_NewWindow("Background Color")
                    display_Title("Background Color",40)
                    Menu_function(BacoMessages,150)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 3:
                    xp=0
                    yp=0  
                    WHITE=colors.get('white')            
                    win.fill(WHITE)
                    create_NewWindow("Background Color")
                    display_Title("Background Color",40)
                    Menu_function(BacoMessages,150)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<545 and yp>445 and counter is 3:    
                    WHITE=colors.get('orange')             
                    win.fill(ORANGE)
                    xp=0
                    yp=0
                    create_NewWindow("Background Color")
                    display_Title("Background Color",40)
                    Menu_function(BacoMessages,150)
                    pygame.display.update()
                    
                if xp >x and xp<x+wbox and yp>y and yp<645 and yp>545 and counter is 3:
                    xp=0
                    yp=0                   
                    win.fill(WHITE)
                    display_Title("Settings",y)
                    Menu_function(settingMessages,150)
                    counter-=2
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<245 and counter is 4:
                    xp=0
                    yp=0  
                    ORANGE=colors.get('orange')                
                    win.fill(WHITE)
                    create_NewWindow("Object Color")
                    display_Title("ObjectColor",40)
                    Menu_function(CoMessages,150)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 4:
                    xp=0
                    yp=0  
                    ORANGE=colors.get('red')             
                    win.fill(ORANGE)
                    create_NewWindow("Object Color")
                    display_Title("Object Color",40)
                    Menu_function(CoMessages,150)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 4:
                    xp=0
                    yp=0  
                    ORANGE=colors.get('white')            
                    win.fill(ORANGE)
                    create_NewWindow("Object Color")
                    display_Title("Object Color",40)
                    Menu_function(CoMessages,150)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<545 and yp>445 and counter is 4:    
                    ORANGE=colors.get('blue')             
                    win.fill(ORANGE)
                    xp=0
                    yp=0
                    create_NewWindow("Object Color")
                    display_Title("Object Color",40)
                    Menu_function(CoMessages,150)
                    pygame.display.update()
                    
                if xp >x and xp<x+wbox and yp>y and yp<645 and yp>545 and counter is 4:
                    xp=0
                    yp=0                   
                    win.fill(WHITE)
                    display_Title("Settings",y)
                    Menu_function(settingMessages,150)
                    counter-=3
                    pygame.time.delay(100)
                    pygame.display.update()
                if xp >x and xp<x+wbox and yp>y and yp<645 and yp>545 and counter is 5:
                    xp=0
                    yp=0 
                    win.fill(WHITE)
                    display_Title("Testy Game",y)
                    Menu_function(gameMessages,150)
                    counter-=5
                    pygame.time.delay(100)
                if xp >x and xp<x+wbox and yp>y and yp<645 and yp>545 and counter is 6:
                    xp=0
                    yp=0 
                    win.fill(WHITE)
                    display_Title("Testy Game",y)
                    Menu_function(gameMessages,150)
                    counter-=6
                    pygame.time.delay(100)
                if xp>x and xp<x+wbox and yp>y and yp<245 and counter is 7 or newgame1==True:
                    walkCount1= 0
                    walkCount2= 0
                    left=False
                    right=False
                    hitstun=False 
                    lastr1= False
                    lastl1= False 
                    lastr2= False
                    lastl2= False
                    if HEIGHT==700:
                        win.blit(sebg,(0,0))
                    if HEIGHT==800:
                        win.blit(eibg(0,0))
                    if HEIGHT==900:
                        win.blit(nibg(0,0))
                    if HEIGHT==1000:
                        win.blit(tebg (0,0))
                    win.blit(StR,FIGx1,FIGy1)
                    win.blit(StL,FIGx2, FIGy2)
                    pygame.draw.rect(win,ORANGE,bolder1)#drawing all of the rectangles with the object colors chosen
                    pygame.draw.rect(win,ORANGE,bolder2)     
                    pygame.draw.rect(win,ORANGE,bolder3)  
                    pygame.draw.rect(win,ORANGE,bolder4)        
                if xp>x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 7 or newgame2==True:
                    walkCount1= 0
                    walkCount2= 0
                    left=False
                    right=False
                    hitstun=False 
                    lastr1= False
                    lastl1= False 
                    lastr2= False
                    lastl2= False
                    if HEIGHT==700:
                        win.blit(sebg2,(0,0))
                    if HEIGHT==800:
                        win.blit(eibg2(0,0))
                    if HEIGHT==900:
                        win.blit(nibg2(0,0))
                    if HEIGHT==1000:
                        win.blit(tebg2 (0,0))
                    win.blit(StR,FIGx1,FIGy1)
                    win.blit(StL,FIGx2, FIGy2)  
                    pygame.draw.rect(win,ORANGE,bolder1)#drawing all of the rectangles with the object colors chosen
                    pygame.draw.rect(win,ORANGE,bolder2)     
                    pygame.draw.rect(win,ORANGE,bolder3)  
                    pygame.draw.rect(win,ORANGE,bolder4)
                                         
                if xp>x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 7:
                    xp=0
                    yp=0 
                    win.fill(WHITE)
                    display_Title("Testy Game",y)
                    Menu_function(gameMessages,150)
                    counter-=7 