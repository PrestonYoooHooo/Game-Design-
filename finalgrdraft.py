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
StL = pygame.image.load('images/716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png 2.jpeg')
StR = pygame.image.load('images/716-7162071_thumb-image-megaman-zero-sprites-hd-png-download.png.jpeg')
sebg = pygame.image.load('images/images copy.jpg')
eibg = pygame.image.load('images/images copy 2.jpg')
nibg = pygame.image.load('images/images copy 3.jpg')
tebg = pygame.image.load('images/images.jpg')
sebg2 = pygame.image.load('images/lava-lake-active-valcano-rj-2560x1700.jpg')
eibg2 = pygame.image.load('images/lava-lake-active-valcano-rj-2560x1700 copy.jpg')
nibg2 = pygame.image.load('images/lava-lake-active-valcano-rj-2560x1700 copy 2.jpg')
tebg2 = pygame.image.load('images/lava-lake-active-valcano-rj-2560x1700 copy 3.jpg')
lamon = pygame.image.load('images/95-957201_lava-muk-pokemon-lava.jpg')
p1 = pygame.image.load('images/pngtree-battle-player-1-vs-2-logo-versus-png-image_2899070.jpeg')
p2 = pygame.image.load('images/pngtree-battle-player-1-vs-2-logo-versus-png-image_2899070.jpeg')
fl = pygame.image.load('images/Unknown.png')#I define/load all of my picture variables 
proj11 = pygame.image.load('images/untitled folder/explosion01_128 copy.png')
proj12 = pygame.image.load('images/untitled folder/explosion01_128 copy 2.png')
proj13 = pygame.image.load('images/untitled folder/explosion01_128 copy 3.png')
proj14 = pygame.image.load('images/untitled folder/explosion01_128 copy 4.png')
proj21 = pygame.image.load("images/untitled folder/explosion01_128 copy 5.png")
proj22 = pygame.image.load('images/untitled folder/explosion01_128 copy 6.png')
proj23 = pygame.image.load('images/untitled folder/explosion01_128 copy 7.png')
proj24 = pygame.image.load('images/untitled folder/explosion01_128 copy 8.png')
p1pjcon=4
p2pjcon=4
projcount11=30
projcount12=30
projcount13=30
projcount14=30
projcount21=30
projcount22=30
projcount23=30
projcount24=30
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
spped1=True
spped2=True
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
porjsped= 15
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Setting Window')
square=pygame.Rect(x,y,wbox,hbox)
#Declare FONTS
TITLE_FONT=pygame.font.SysFont('comicsans',80)
SubTitle=pygame.font.SysFont('comicsans', 40, italic=True)
MENU_FONT=pygame.font.SysFont('comicsans',40)
INSTUR_FONT=pygame.font.SysFont('comicsans',30)
text=TITLE_FONT.render('message',1,BLACK)
pj11=False
pj12=False
pj13=False
pj14=False
pj21=False
pj22=False
pj23=False
pj24=False
counter=0
walkCount1= 0
walkCount2= 0
left1=False
right1=False
left2=False
right2=False
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
    if left1==True and right1==False:  #for every time they take a step the walkcount is moved up by one and their image is changed constanly to make it look like they are moving in a certian direction
        win.blit(walkLeft[walkCount//3], (FIGx1,FIGy1))
        walkCount += 1                          
    elif right1==True and left1 ==False:
        win.blit(walkRight[walkCount//3], (FIGx1,FIGy1))
        walkCount += 1
    elif lastr1== True and lastl1 == False:
        win.blit(StR, (FIGx1, FIGy1))
        walkCount = 0
    else:
        win.blit(StL,FIGx1,FIGy1)
        walkCount=0
    if pj11==True:
        win.blit(proj11,pjxl11,pjy11)
    if pj12==True:
        win.blit(proj12,pjxl12,pjy12)
    if pj13==True:
        win.blit(proj13,pjxl13,pjy13)
    if pj14==True:
        win.blit(proj14,pjxl14,pjy14)
    if pj21==True:
        win.blit(proj21,pjxl21,pjy21)
    if pj22==True:
        win.blit(proj22,pjxl22,pjy22)
    if pj23==True:
        win.blit(proj23,pjxl23,pjy23)
    if pj24==True:
        win.blit(proj24,pjxl24,pjy24)
def redrawGameWindowforp2():
    global walkCount1 
    if walkCount1 + 1 >= 27:
        walkCount = 0 
    if left2==True and right2==False:  
        win.blit(walkLeft[walkCount//3], (FIGx2,FIGy2))
        walkCount += 1                          
    elif right2==True and left2 ==False:
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
                    boldx1=200
                    boldy1=200
                    boldx2=WIDTH-200
                    boldy2=200
                    boldy3=HEIGHT-200
                    boldx3=200
                    boldx4=WIDTH-200
                    boldy4=HEIGHT-200
                    left1=False
                    right1=False
                    left2=False
                    Right2=False
                    hitstun=False 
                    lastr1= True
                    lastl1= False 
                    lastr2= False
                    lastl2= True
                    lastw1=False
                    lastw2=False
                    lastd1=False
                    lastd2=False
                    P1x=FIGx1
                    P2x=FIGx2
                    P1y=FIGy1-45
                    P2y=FIGy2-45
                    pjxr11=FIGx1-40
                    pjy11=FIGy1
                    pjxl11=FIGx1+40
                    pjxr21=FIGx2-40
                    pjy21=FIGy2
                    pjxl21=FIGx2+40
                    pjxr12=FIGx1-40
                    pjy12=FIGy1
                    pjxl12=FIGx1+40
                    pjxr22=FIGx2-40
                    pjy22=FIGy2
                    pjxl22=FIGx2+40
                    pjxr13=FIGx1-40
                    pjy13=FIGy1
                    pjxl13=FIGx1+40
                    pjxr23=FIGx2-40
                    pjy23=FIGy2
                    pjxl23=FIGx2+40
                    pjxr14=FIGx1-40
                    pjy14=FIGy1
                    pjxl14=FIGx1+40
                    pjxr24=FIGx2-40
                    pjy24=FIGy2
                    pjxl24=FIGx2+40
                    pjyw11=FIGy1-40
                    pjyw12=FIGy1-40
                    pjyw13=FIGy1-40
                    pjyw14=FIGy1-40
                    pjyw21=FIGy2-40
                    pjyw22=FIGy2-40
                    pjyw23=FIGy2-40
                    pjyw24=FIGy2-40
                    pjyd11=FIGy1+40
                    pjyd11=FIGy1+40
                    pjyd12=FIGy1+40
                    pjyd13=FIGy1+40
                    pjyd14=FIGy1+40
                    pjyd21=FIGy2+40
                    pjyd22=FIGy2+40
                    pjyd23=FIGy2+40
                    pjyd24=FIGy2+40
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
                    win.blit(p1,P1x,P1y)
                    win.blit(p2,P2x, P2y)
                    pygame.draw.rect(win,ORANGE,bolder1)#drawing all of the rectangles with the object colors chosen
                    pygame.draw.rect(win,ORANGE,bolder2)     
                    pygame.draw.rect(win,ORANGE,bolder3)  
                    pygame.draw.rect(win,ORANGE,bolder4)
                    while play:
                            pygame.time.delay(100) #milliseconds 
                            for anyThing in pygame.event.get(): #variable for anytrhing that happneds in py to listen to keyboard and mouse
                                if anyThing.type ==pygame.QUIT: #says if Quit is typed something happends
                                    run =False
                            keyPressed= pygame.key.get_pressed()#records keyboard movement
                            speedx=10
                            speedy=10
                            P1y=FIGy1-45
                            P2y=FIGy2-45
                            if spped1==True:  
                                if keyPressed[pygame.K_RIGHT]:  
                                    FIGx1 +=speedx 
                                    right1=True
                                    left1=False
                                    lastr1=True
                                    lastl1=False
                                    lastd1=False
                                    lastw1=False
                                if keyPressed[pygame.K_LEFT]:  
                                    FIGx1 -=speedx 
                                    right1=False
                                    left1=True
                                    lastr1=False
                                    lastl1=True
                                    lastd1=False
                                    lastw1=False
                                if keyPressed[pygame.K_UP]:  
                                    FIGy1-=speedx
                                    lastr1=False
                                    lastl1=False
                                    lastd1=False
                                    lastw1=True
                                if keyPressed [pygame.K_DOWN]:
                                    FIGy1 +=speedx
                                    lastr1=False
                                    lastl1=False
                                    lastw1=False
                                    lastd1=True
                                if keyPressed[pygame.K_f]:
                                    if lastr1==True and p1pjcon>0:
                                        if p1pjcon==4:
                                            win.blit(proj11,pjxr11,FIGy1)
                                            p1pjcon-=1
                                            pj11=True
                                        if p1pjcon==3:
                                            win.blit(proj12,pjxr12,FIGy1)
                                            p1pjcon-=1  
                                            pj12=True  
                                        if p1pjcon==2:
                                            win.blit(proj13,pjxr13,FIGy1)
                                            p1pjcon-=1 
                                            pj13=True
                                        if p1pjcon==1:
                                            win.blit(proj14,pjxr14,FIGy1)
                                            p1pjcon-=1 
                                            pj14=True
                                    if lastl1==True and p1pjcon>0:
                                        if p1pjcon==4:
                                            win.blit(proj11,pjxl11,FIGy1)
                                            p1pjcon-=1
                                            pj11=True
                                        if p1pjcon==3:
                                            win.blit(proj12,pjxl12,FIGy1)
                                            p1pjcon-=1 
                                            pj12=True    
                                        if p1pjcon==2:
                                            win.blit(proj13,pjxl13,FIGy1)
                                            p1pjcon-=1 
                                            pj13=True
                                        if p1pjcon==1:
                                            win.blit(proj14,pjxl14,FIGy1)
                                            p1pjcon-=1 
                                            pj14=True 
                            if spped2==True:
                                if keyPressed[pygame.K_d]:  
                                    FIGx2 +=speedy 
                                    righ2=True
                                    left2=False
                                    lastr2=True
                                    lastl2=False 
                                    lastd2=False
                                    lastw2=False
                                if keyPressed[pygame.K_a]:  
                                    FIGx2-=speedy
                                    right2=False
                                    left2=True
                                    lastr2=False
                                    lastl2=True
                                    lastd2=False
                                    lastw2=False
                                if keyPressed[pygame.K_w]:  
                                    FIGy2-=speedy
                                    lastr2=False
                                    lastl2=False
                                    lastd2=False
                                    lastw2=True
                                if keyPressed[pygame.K_s]:
                                    FIGy2 +=speedy
                                    lastr2=False
                                    lastl2=False
                                    lastd2=True
                                    lastw2=False
                                if keyPressed[pygame.K_SLASH]:
                                    if lastr2==True and p2pjcon>0:
                                        if p2pjcon==4:
                                            win.blit(proj21,pjxr21,pjy11)
                                            p2pjcon-=1
                                            pj21=True
                                        if p2pjcon==3:
                                            win.blit(proj22,pjxr22,pjy12)
                                            p2pjcon-=1 
                                            pj22=True    
                                        if p2pjcon==2:
                                            win.blit(proj23,pjxr23,pjy13)
                                            p2pjcon-=1 
                                            pj23=True
                                        if p2pjcon==1:
                                            win.blit(proj24,pjxr24,pjy14)
                                            p2pjcon-=1
                                            pj24=True 
                                    if lastl2==True and p2pjcon>0:
                                        if p2pjcon==4:
                                            win.blit(proj21,pjxr21,pjy21)
                                            p2pjcon-=1
                                            pj21=True
                                        if p2pjcon==3:
                                            win.blit(proj22,pjxr22,pjy22)
                                            p2pjcon-=1  
                                            pj22=True   
                                        if p2pjcon==2:
                                            win.blit(proj23,pjxr23,pjy23)
                                            p2pjcon-=1 
                                            pj23=True
                                        if p2pjcon==1:
                                            win.blit(proj24,pjxr24,pjy24)
                                            p2pjcon-=1 
                                            pj24=True
                            if pj11==True and projcount11>0 and lastl1==True:
                                pjxl11+=20
                                projcount11-=1
                                if pjxl11 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj11==False
                                    projcount11=30
                                    pjxl11=FIGx1-40
                                    pjy11=FIGy1
                                if pjy11 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj11==False
                                    projcount11=30
                                    pjxl11=FIGx1-40  
                                    pjy11=FIGy1  
                                if pjxl11 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj11==False
                                    projcount11=30
                                    pjxl11=FIGx1-40
                                    pjy11=FIGy1
                                if pjy11 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj11==False
                                    projcount11=30
                                    pjxl11=FIGx1-40  
                                    pjy11=FIGy1  
                            elif pj11==False or projcount11<1:
                                pj11=False
                                projcount11=30
                                pjxl11=FIGx1-40  
                                pjy11=FIGy1 
                            if pj12==True and projcount12>0 and lastl1==True:
                                pjxl12+=20
                                projcount12-=1
                                if pjxl12 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj12==False
                                    projcount12=30
                                    pjxl12=FIGx1-40
                                    pjy12=FIGy1
                                if pjy12 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj12==False
                                    projcount12=30
                                    pjxl12=FIGx1-40  
                                    pjy12=FIGy1  
                                if pjxl12 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj12==False
                                    projcount12=30
                                    pjxl12=FIGx1-40
                                    pjy12=FIGy1
                                if pjy12 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj12==False
                                    projcount12=30
                                    pjxl12=FIGx1-40  
                                    pjy12=FIGy1  
                            elif pj12==False or projcount12<1:
                                pj12=False
                                projcount12=30
                                pjxl12=FIGx1-40  
                                pjy12=FIGy1
                            if pj13==True and projcount13>0 and lastl1==True:
                                pjxl13+=20
                                projcount13-=1
                                if pjxl13 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj13==False
                                    projcount13=30
                                    pjxl13=FIGx1-40
                                    pjy13=FIGy1
                                if pjy13 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj13==False
                                    projcount13=30
                                    pjxl13=FIGx1-40  
                                    pjy13=FIGy1  
                                if pjxl13 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj13==False
                                    projcount13=30
                                    pjxl13=FIGx1-40
                                    pjy13=FIGy1
                                if pjy13 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj13==False
                                    projcount13=30
                                    pjxl13=FIGx1-40  
                                    pjy13=FIGy1 
                            elif pj13==False or projcount13<1:
                                pj13=False
                                projcount13=30
                                pjxl13=FIGx1-40  
                                pjy13=FIGy1
                            if pj14==True and projcount13>0 and lastl1==True:
                                pjxl14+=20
                                projcount14-=1
                                if pjxl14 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj14==False
                                    projcount14=30
                                    pjxl14=FIGx1-40
                                    pjy14=FIGy1
                                if pjy14 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj14==False
                                    projcount14=30
                                    pjxl14=FIGx1-40  
                                    pjy14=FIGy1  
                                if pjxl14 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj14==False
                                    projcount14=30
                                    pjxl14=FIGx1-40
                                    pjy14=FIGy1
                                if pjy14 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj14==False
                                    projcount14=30
                                    pjxl14=FIGx1-40  
                                    pjy14=FIGy1  
                            elif pj14==False or projcount14<1:
                                pj14=False
                                projcount14=30
                                pjxl14=FIGx1-40  
                                pjy14=FIGy1
                            if pj21==True and projcount21>0 and lastl2==True:
                                pjxl21+=20
                                projcount21-=1
                                if pjxl21 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj21==False
                                    projcount21=30
                                    pjxl21=FIGx2-40
                                    pjy21=FIGy2
                                if pjy21 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj21==False
                                    projcount21=30
                                    pjxl21=FIGx2-40  
                                    pjy21=FIGy2  
                                if pjxl21 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj21==False
                                    projcount21=30
                                    pjxl21=FIGx2-40
                                    pjy21=FIGy2
                                if pjy21 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj21==False
                                    projcount21=30
                                    pjxl21=FIGx2-40  
                                    pjy21=FIGy2  
                            elif pj21==False or projcount21<1:
                                pj21=False
                                projcount21=30
                                pjxl21=FIGx2-40  
                                pjy21=FIGy2 
                            if pj22==True and projcount22>0 and lastl2==True:
                                pjxl22+=20
                                projcount22-=1
                                if pjxl22 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj22==False
                                    projcount22=30
                                    pjxl22=FIGx2-40
                                    pjy22=FIGy2
                                if pjy22 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj22==False
                                    projcount22=30
                                    pjxl22=FIGx2-40  
                                    pjy22=FIGy2  
                                if pjxl22 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj22==False
                                    projcount22=30
                                    pjxl22=FIGx2-40
                                    pjy22=FIGy2
                                if pjy22 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj22==False
                                    projcount22=30
                                    pjxl22=FIGx2-40  
                                    pjy22=FIGy2  
                            elif pj22==False or projcount22<1:
                                pj22=False
                                projcount22=30
                                pjxl22=FIGx2-40  
                                pjy22=FIGy2 
                            if pj23==True and projcount23>0 and lastl2==True:
                                pjxl23+=20
                                projcount23-=1
                                if pjxl23 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj23==False
                                    projcount23=30
                                    pjxl23=FIGx2-40
                                    pjy23=FIGy2
                                if pjy23 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj23==False
                                    projcount23=30
                                    pjxl23=FIGx2-40  
                                    pjy23=FIGy2  
                                if pjxl23 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj23==False
                                    projcount23=30
                                    pjxl23=FIGx2-40
                                    pjy23=FIGy2
                                if pjy23 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj23==False
                                    projcount23=30
                                    pjxl23=FIGx2-40  
                                    pjy23=FIGy2  
                            elif pj23==False or projcount23<1:
                                pj23=False
                                projcount23=30
                                pjxl23=FIGx2-40  
                                pjy23=FIGy2 
                            if pj24==True and projcount24>0 and lastl2==True:
                                pjxl24+=20
                                projcount24-=1
                                if pjxl24 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj24==False
                                    projcount24=30
                                    pjxl24=FIGx2-40
                                    pjy24=FIGy2
                                if pjy24 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj24==False
                                    projcount24=30
                                    pjxl24=FIGx2-40  
                                    pjy24=FIGy2  
                                if pjxl24 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj24==False
                                    projcount24=30
                                    pjxl24=FIGx2-40
                                    pjy24=FIGy2
                                if pjy24 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj24==False
                                    projcount24=30
                                    pjxl24=FIGx2-40  
                                    pjy24=FIGy2  
                            elif pj24==False or projcount24<1:
                                pj24=False
                                projcount24=30
                                pjxl24=FIGx2-40  
                                pjy24=FIGy2 
                            if pj11==True and projcount11>0 and lastr1==True:
                                pjxr11+=20
                                projcount11-=1
                                if pjxr11 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj11==False
                                    projcount11=30
                                    pjxr11=FIGx1+40
                                    pjy11=FIGy1
                                if pjy11 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj11==False
                                    projcount11=30
                                    pjxr11=FIGx1+40  
                                    pjy11=FIGy1  
                                if pjxr11 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj11==False
                                    projcount11=30
                                    pjxr11=FIGx1+40
                                    pjy11=FIGy1
                                if pjy11 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj11==False
                                    projcount11=30
                                    pjxr11=FIGx1+40  
                                    pjy11=FIGy1  
                            elif pj11==False or projcount11<1:
                                pj11=False
                                projcount11=30
                                pjxr11=FIGx1+40  
                                pjy11=FIGy1 
                            if pj12==True and projcount12>0 and lastr1==True:
                                pjxr12+=20
                                projcount12-=1
                                if pjxr12 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj12==False
                                    projcount12=30
                                    pjxr12=FIGx1+40
                                    pjy12=FIGy1
                                if pjy12 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj12==False
                                    projcount12=30
                                    pjxr12=FIGx1+40  
                                    pjy12=FIGy1  
                                if pjxr12 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj12==False
                                    projcount12=30
                                    pjxr12=FIGx1+40
                                    pjy12=FIGy1
                                if pjy12 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj12==False
                                    projcount12=30
                                    pjxr12=FIGx1+40  
                                    pjy12=FIGy1  
                            elif pj12==False or projcount12<1:
                                pj12=False
                                projcount12=30
                                pjxr12=FIGx1+40  
                                pjy12=FIGy1
                            if pj13==True and projcount13>0 and lastr1==True:
                                pjxr13+=20
                                projcount13-=1
                                if pjxr13 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj13==False
                                    projcount13=30
                                    pjxr13=FIGx1+40
                                    pjy13=FIGy1
                                if pjy13 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj13==False
                                    projcount13=30
                                    pjxr13=FIGx1-40  
                                    pjy13=FIGy1  
                                if pjxr13 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj13==False
                                    projcount13=30
                                    pjxr13=FIGx1-40
                                    pjy13=FIGy1
                                if pjy13 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj13==False
                                    projcount13=30
                                    pjxr13=FIGx1-40  
                                    pjy13=FIGy1 
                            elif pj13==False or projcount13<1:
                                pj13=False
                                projcount13=30
                                pjxr13=FIGx1-40  
                                pjy13=FIGy1
                            if pj14==True and projcount13>0 and lastr1==True:
                                pjxr14+=20
                                projcount14-=1
                                if pjxr14 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj14==False
                                    projcount14=30
                                    pjxr14=FIGx1+40
                                    pjy14=FIGy1
                                if pjy14 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj14==False
                                    projcount14=30
                                    pjxr14=FIGx1+40  
                                    pjy14=FIGy1  
                                if pjxr14 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj14==False
                                    projcount14=30
                                    pjxr14=FIGx1+40
                                    pjy14=FIGy1
                                if pjy14 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj14==False
                                    projcount14=30
                                    pjxr14=FIGx1+40  
                                    pjy14=FIGy1  
                            elif pj14==False or projcount14<1:
                                pj14=False
                                projcount14=30
                                pjxr14=FIGx1+40  
                                pjy14=FIGy1
                            if pj21==True and projcount21>0 and lastr2==True:
                                pjxr21+=20
                                projcount21-=1
                                if pjxr21 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj21==False
                                    projcount21=30
                                    pjxr21=FIGx2+40
                                    pjy21=FIGy2
                                if pjy21 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj21==False
                                    projcount21=30
                                    pjxr21=FIGx2+40  
                                    pjy21=FIGy2  
                                if pjxr21 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj21==False
                                    projcount21=30
                                    pjxr21=FIGx2+40
                                    pjy21=FIGy2
                                if pjy21 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj21==False
                                    projcount21=30
                                    pjxr21=FIGx2+40  
                                    pjy21=FIGy2  
                            elif pj21==False or projcount21<1:
                                pj21=False
                                projcount21=30
                                pjxr21=FIGx2-40  
                                pjy21=FIGy2 
                            if pj22==True and projcount22>0 and lastr2==True:
                                pjxr22+=20
                                projcount22-=1
                                if pjxr22 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj22==False
                                    projcount22=30
                                    pjxr22=FIGx2+40
                                    pjy22=FIGy2
                                if pjy22 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj22==False
                                    projcount22=30
                                    pjxr22=FIGx2+40  
                                    pjy22=FIGy2  
                                if pjxr22 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj22==False
                                    projcount22=30
                                    pjxr22=FIGx2+40
                                    pjy22=FIGy2
                                if pjy22 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj22==False
                                    projcount22=30
                                    pjxr22=FIGx2+40  
                                    pjy22=FIGy2  
                            elif pj22==False or projcount22<1:
                                pj22=False
                                projcount22=30
                                pjxr22=FIGx2+40  
                                pjy22=FIGy2 
                            if pj23==True and projcount23>0 and lastr2==True:
                                pjxr23+=20
                                projcount23-=1
                                if pjxr23 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj23==False
                                    projcount23=30
                                    pjxr23=FIGx2+40
                                    pjy23=FIGy2
                                if pjy23 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj23==False
                                    projcount23=30
                                    pjxr23=FIGx2+40  
                                    pjy23=FIGy2  
                                if pjxr23 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj23==False
                                    projcount23=30
                                    pjxr23=FIGx2+40
                                    pjy23=FIGy2
                                if pjy23 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj23==False
                                    projcount23=30
                                    pjxr23=FIGx2+40  
                                    pjy23=FIGy2  
                            elif pj23==False or projcount23<1:
                                pj23=False
                                projcount23=30
                                pjxr23=FIGx2+40  
                                pjy23=FIGy2 
                            if pj24==True and projcount24>0 and lastr2==True:
                                pjxr24+=20
                                projcount24-=1
                                if pjxr24 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj24==False
                                    projcount24=30
                                    pjxr24=FIGx2+40
                                    pjy24=FIGy2
                                if pjy24 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj24==False
                                    projcount24=30
                                    pjxr24=FIGx2+40  
                                    pjy24=FIGy2  
                                if pjxr24 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj24==False
                                    projcount24=30
                                    pjxr24=FIGx2+40
                                    pjy24=FIGy2
                                if pjy24 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj24==False
                                    projcount24=30
                                    pjxr24=FIGx2+40  
                                    pjy24=FIGy2  
                            elif pj24==False or projcount24<1:
                                pj24=False
                                projcount24=30
                                pjxr24=FIGx2+40  
                                pjy24=FIGy2 
                            if pj11==True and projcount11>0 and lastw1==True:
                                pjy11-=20
                                projcount11-=1
                                if pjy11 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj11==False
                                    projcount11=30
                                    pjy11=FIGy1-40
                                if pjy11 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj11==False
                                    projcount11=30
                                    pjy11=FIGy1-40   
                                if pjy11 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj11==False
                                    projcount11=30
                                    pjy11=FIGy1-40
                                if pjy11 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj11==False
                                    projcount11=30
                                    pjy11=FIGy1-40   
                            elif pj11==False or projcount11<1:
                                pj11=False
                                projcount11=30
                                pjy11=FIGy1-40 
                            if pj12==True and projcount12>0 and lastw1==True:
                                pjy12-=20
                                projcount12-=1
                                if pjy12 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj12==False
                                    projcount12=30
                                    pjy12=FIGy1-40
                                if pjy12 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj12==False
                                    projcount12=30
                                    pjy12=FIGy1-40   
                                if pjy12 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj12==False
                                    projcount12=30
                                    pjy12=FIGy1-40
                                if pjy12 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj12==False
                                    projcount12=30
                                    pjy12=FIGy1-40   
                            elif pj12==False or projcount12<1:
                                pj12=False
                                projcount12=30
                                pjy12=FIGy1-40 
                            if pj13==True and projcount13>0 and lastw1==True:
                                pjy13-=20
                                projcount13-=1
                                if pjy13 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj13==False
                                    projcount13=30
                                    pjy13=FIGy1-40
                                if pjy13 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj13==False
                                    projcount13=30
                                    pjy13=FIGy1-40   
                                if pjy13 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj13==False
                                    projcount13=30
                                    pjy13=FIGx1-40
                                if pjy13 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj13==False
                                    projcount13=30
                                    pjy13=FIGy1-40  
                            elif pj13==False or projcount13<1:
                                pj13=False
                                projcount13=30
                                pjy13=FIGy1-40
                            if pj14==True and projcount13>0 and lastw1==True:
                                pjy14-=20
                                projcount14-=1
                                if pjy14 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj14==False
                                    projcount14=30
                                    pjy14=FIGy1-40
                                if pjy14 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj14==False
                                    projcount14=30
                                    pjy14=FIGy1-40    
                                if pjy14 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj14==False
                                    projcount14=30
                                    pjy14=FIGy1-40
                                if pjy14 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj14==False
                                    projcount14=30
                                    pjy14=FIGy1-40    
                            elif pj14==False or projcount14<1:
                                pj14=False
                                projcount14=30
                                pjy14=FIGy1-40 
                            if pj21==True and projcount21>0 and lastw2==True:
                                pjy21-=20
                                projcount21-=1
                                if pjy21 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj21==False
                                    projcount21=30
                                    pjy21=FIGy2-40
                                if pjy21 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj21==False
                                    projcount21=30
                                    pjy21=FIGy2-40   
                                if pjy21 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj21==False
                                    projcount21=30
                                    pjy21=FIGy2-40
                                if pjy21 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj21==False
                                    projcount21=30
                                    pjy21=FIGy2-40  
                            elif pj21==False or projcount21<1:
                                pj21=False
                                projcount21=30
                                pjy21=FIGx2-40  
                            if pj22==True and projcount22>0 and lastw2==True:
                                pjy22-=20
                                projcount22-=1
                                if pjy22 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj22==False
                                    projcount22=30
                                    pjy22=FIGy2-40
                                if pjy22 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj22==False
                                    projcount22=30
                                    pjy22=FIGy2-40  
                                if pjy22 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj22==False
                                    projcount22=30
                                    pjy22=FIGy2-40
                                if pjy22 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj22==False
                                    projcount22=30
                                    pjy22=FIGy2-40  
                            elif pj22==False or projcount22<1:
                                pj22=False
                                projcount22=30
                                pjy22=FIGy2-40  
                            if pj23==True and projcount23>0 and lastw2==True:
                                pjy23-=20
                                projcount23-=1
                                if pjy23 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj23==False
                                    projcount23=30
                                    pjy23=FIGy2-40
                                if pjy23 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj23==False
                                    projcount23=30
                                    pjy23=FIGy2-40    
                                if pjy23 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj23==False
                                    projcount23=30
                                    pjy23=FIGy2-40
                                if pjy23 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj23==False
                                    projcount23=30
                                    pjy23=FIGy2-40   
                            elif pj23==False or projcount23<1:
                                pj23=False
                                projcount23=30
                                pjy23=FIGy2-40  
                            if pj24==True and projcount24>0 and lastw2==True:
                                pjy24-=20
                                projcount24-=1
                                if pjy24 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj24==False
                                    projcount24=30
                                    pjy24=FIGy2-40
                                if pjy24 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj24==False
                                    projcount24=30
                                    pjy24=FIGy2-40  
                                if pjy24 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj24==False
                                    projcount24=30
                                    pjy24=FIGy2-40
                                if pjy24 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj24==False
                                    projcount24=30
                                    pjy24=FIGy2-40  
                            elif pj24==False or projcount24<1:
                                pj24=False
                                projcount24=30
                                pjy24=FIGy2-40  
                            if pj11==True and projcount11>0 and lastd1==True:
                                pjy11+=20
                                projcount11-=1
                                if pjy11 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj11==False
                                    projcount11=30
                                    pjy11=FIGy1+40
                                if pjy11 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj11==False
                                    projcount11=30
                                    pjy11=FIGy1+40   
                                if pjy11 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj11==False
                                    projcount11=30
                                    pjy11=FIGy1+40
                                if pjy11 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj11==False
                                    projcount11=30
                                    pjy11=FIGy1+40   
                            elif pj11==False or projcount11<1:
                                pj11=False
                                projcount11=30
                                pjy11=FIGy1+40 
                            if pj12==True and projcount12>0 and lastd1==True:
                                pjy12+=20
                                projcount12-=1
                                if pjy12 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj12==False
                                    projcount12=30
                                    pjy12=FIGy1+40
                                if pjy12 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj12==False
                                    projcount12=30
                                    pjy12=FIGy1+40   
                                if pjy12 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj12==False
                                    projcount12=30
                                    pjy12=FIGy1+40
                                if pjy12 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj12==False
                                    projcount12=30
                                    pjy12=FIGy1+40   
                            elif pj12==False or projcount12<1:
                                pj12=False
                                projcount12=30
                                pjy12=FIGy1+40 
                            if pj13==True and projcount13>0 and lastd1==True:
                                pjy13+=20
                                projcount13-=1
                                if pjy13 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj13==False
                                    projcount13=30
                                    pjy13=FIGy1+40
                                if pjy13 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj13==False
                                    projcount13=30
                                    pjy13=FIGy1+40   
                                if pjy13 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj13==False
                                    projcount13=30
                                    pjy13=FIGx1+40
                                if pjy13 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj13==False
                                    projcount13=30
                                    pjy13=FIGy1+40  
                            elif pj13==False or projcount13<1:
                                pj13=False
                                projcount13=30
                                pjy13=FIGy1+40
                            if pj14==True and projcount13>0 and lastd1==True:
                                pjy14+=20
                                projcount14-=1
                                if pjy14 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj14==False
                                    projcount14=30
                                    pjy14=FIGy1+40
                                if pjy14 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj14==False
                                    projcount14=30
                                    pjy14=FIGy1+40    
                                if pjy14 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj14==False
                                    projcount14=30
                                    pjy14=FIGy1+40
                                if pjy14 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj14==False
                                    projcount14=30
                                    pjy14=FIGy1+40    
                            elif pj14==False or projcount14<1:
                                pj14=False
                                projcount14=30
                                pjy14=FIGy1+40 
                            if pj21==True and projcount21>0 and lastd2==True:
                                pjy21+=20
                                projcount21-=1
                                if pjy21 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj21==False
                                    projcount21=30
                                    pjy21=FIGy2+40
                                if pjy21 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj21==False
                                    projcount21=30
                                    pjy21=FIGy2+40   
                                if pjy21 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj21==False
                                    projcount21=30
                                    pjy21=FIGy2+40
                                if pjy21 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj21==False
                                    projcount21=30
                                    pjy21=FIGy2+40  
                            elif pj21==False or projcount21<1:
                                pj21=False
                                projcount21=30
                                pjy21=FIGx2+40  
                            if pj22==True and projcount22>0 and lastd2==True:
                                pjy22+=20
                                projcount22-=1
                                if pjy22 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj22==False
                                    projcount22=30
                                    pjy22=FIGy2+40
                                if pjy22 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj22==False
                                    projcount22=30
                                    pjy22=FIGy2+40  
                                if pjy22 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj22==False
                                    projcount22=30
                                    pjy22=FIGy2+40
                                if pjy22 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj22==False
                                    projcount22=30
                                    pjy22=FIGy2+40  
                            elif pj22==False or projcount22<1:
                                pj22=False
                                projcount22=30
                                pjy22=FIGy2+40  
                            if pj23==True and projcount23>0 and lastd2==True:
                                pjy23+=20
                                projcount23-=1
                                if pjy23 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj23==False
                                    projcount23=30
                                    pjy23=FIGy2+40
                                if pjy23 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj23==False
                                    projcount23=30
                                    pjy23=FIGy2+40    
                                if pjy23 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj23==False
                                    projcount23=30
                                    pjy23=FIGy2+40
                                if pjy23 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj23==False
                                    projcount23=30
                                    pjy23=FIGy2+40   
                            elif pj23==False or projcount23<1:
                                pj23=False
                                projcount23=30
                                pjy23=FIGy2+40  
                            if pj24==True and projcount24>0 and lastd2==True:
                                pjy24+=20
                                projcount24-=1
                                if pjy24 == boldx1+80 or boldx2+80 or boldx3+80 or boldx4+80:
                                    pj24==False
                                    projcount24=30
                                    pjy24=FIGy2+40                                   
                                if pjy24 == boldy1+80 or boldy2+80 or boldy3+80 or boldy4+80:
                                    pj24==False
                                    projcount24=30
                                    pjy24=FIGy2+40                                       
                                if pjy24 == boldx1-80 or boldx2-80 or boldx3-80 or boldx4-80:
                                    pj24==False
                                    projcount24=30
                                    pjy24=FIGy2+40
                                if pjy24 == boldy1-80 or boldy2-80 or boldy3-80 or boldy4-80:
                                    pj24==False
                                    projcount24=30
                                    pjy24=FIGy2+40  
                            elif pj24==False or projcount24<1:
                                pj24=False
                                projcount24=30
                                pjy24=FIGy2+40  
                            if FIGx1==boldx1+85 or boldx2+85 or boldx3+85 or boldx4+85 or boldx1-85 or boldx2-85 or boldx3-85 or boldx4-85:
                                spped1=False
                                pygame.time.delay(3000)
                                spped1=True
                            if FIGy1==boldy1+85 or boldy2+85 or boldy3+85 or boldy4+85 or boldy1-85 or boldy2-85 or boldy3-85 or boldy4-85:
                                spped1=False
                                pygame.time.delay(3000)
                                spped1=True
                            if FIGx2==boldx1+85 or boldx2+85 or boldx3+85 or boldx4+85 or boldx1-85 or boldx2-85 or boldx3-85 or boldx4-85:
                                spped2=False
                                pygame.time.delay(3000)
                                spped2=True
                            if FIGy2==boldy1+85 or boldy2+85 or boldy3+85 or boldy4+85 or boldy1-85 or boldy2-85 or boldy3-85 or boldy4-85:
                                spped2=False
                                pygame.time.delay(3000)
                                spped2=True
                if xp>x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 7 or newgame2==True:
                    walkCount1= 0
                    walkCount2= 0
                    left1=False
                    right1=False
                    left2=False
                    Right2=False
                    hitstun=False 
                    lastr1= True
                    lastl1= False 
                    lastr2= False
                    lastl2= True
                    lastw1=False
                    lastw2=False
                    lastd1=False
                    lastd2=False
                    pjxr11=FIGx1-40
                    pjy11=FIGy1
                    pjxl11=FIGx1+40
                    pjxr21=FIGx2-40
                    pjy21=FIGy2
                    pjxl21=FIGx2+40
                    pjxr12=FIGx1-40
                    pjy12=FIGy1
                    pjxl12=FIGx1+40
                    pjxr22=FIGx2-40
                    pjy22=FIGy2
                    pjxl22=FIGx2+40
                    pjxr13=FIGx1-40
                    pjy13=FIGy1
                    pjxl13=FIGx1+40
                    pjxr23=FIGx2-40
                    pjy23=FIGy2
                    pjxl23=FIGx2+40
                    pjxr14=FIGx1-40
                    pjy14=FIGy1
                    pjxl14=FIGx1+40
                    pjxr24=FIGx2-40
                    pjy24=FIGy2
                    pjxl24=FIGx2+40
                    pjyw11=FIGy1-40
                    pjyw12=FIGy1-40
                    pjyw13=FIGy1-40
                    pjyw14=FIGy1-40
                    pjyw21=FIGy2-40
                    pjyw22=FIGy2-40
                    pjyw23=FIGy2-40
                    pjyw24=FIGy2-40
                    pjyd11=FIGy1+40
                    pjyd11=FIGy1+40
                    pjyd12=FIGy1+40
                    pjyd13=FIGy1+40
                    pjyd14=FIGy1+40
                    pjyd21=FIGy2+40
                    pjyd22=FIGy2+40
                    pjyd23=FIGy2+40
                    pjyd24=FIGy2+40
                    boldx1=200
                    boldy1=200
                    boldx2=WIDTH-200
                    boldy2=200
                    boldy3=HEIGHT-200
                    boldx3=200
                    boldx4=WIDTH-200
                    boldy4=HEIGHT-200
                    P1x=FIGx1
                    P2x=FIGx2
                    P1y=FIGy1-45
                    P2y=FIGy2-45
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
                    win.blit(p1,P1x,P1y)
                    win.blit(p2,P2x, P2y) 
                    pygame.draw.rect(win,ORANGE,bolder1)#drawing all of the rectangles with the object colors chosen
                    pygame.draw.rect(win,ORANGE,bolder2)     
                    pygame.draw.rect(win,ORANGE,bolder3)  
                    pygame.draw.rect(win,ORANGE,bolder4)
                    while play:
                            pygame.time.delay(100) #milliseconds 
                            for anyThing in pygame.event.get(): #variable for anytrhing that happneds in py to listen to keyboard and mouse
                                if anyThing.type ==pygame.QUIT: #says if Quit is typed something happends
                                    run =False
                            keyPressed= pygame.key.get_pressed()#records keyboard movement
                            speedx=10
                            speedy=10 
                            if spped1==True:
                                if keyPressed[pygame.K_RIGHT]:  
                                    FIGx1 +=speedx 
                                    right1=True
                                    left1=False
                                    lastr1=True
                                    lastl1=False 
                                    lastd1=False
                                    lastw1=False
                                if keyPressed[pygame.K_LEFT]:  
                                    FIGx1 -=speedx 
                                    right1=False
                                    left1=True
                                    lastr1=False
                                    lastl1=True
                                    lastd1=False
                                    lastw1=False
                                if keyPressed[pygame.K_UP]:  
                                    FIGy1-=speedx
                                    lastr1=False
                                    lastl1=False
                                    lastd1=False
                                    lastw1=True
                                if keyPressed [pygame.K_DOWN]:
                                    FIGy1 +=speedx
                                    lastr1=False
                                    lastl1=False
                                    lastd1=True
                                    lastw1=False
                                if keyPressed[pygame.K_f]:
                                    if lastr1==True and p1pjcon>0:
                                        if p1pjcon==4:
                                            win.blit(proj11,pjxr11,FIGy1)
                                            p1pjcon-=1
                                            pj11=True
                                        if p1pjcon==3:
                                            win.blit(proj12,pjxr12,FIGy1)
                                            p1pjcon-=1  
                                            pj12=True   
                                        if p1pjcon==2:
                                            win.blit(proj13,pjxr13,FIGy1)
                                            p1pjcon-=1
                                            pj13=True 
                                        if p1pjcon==1:
                                            win.blit(proj14,pjxr14,FIGy1)
                                            p1pjcon-=1
                                            pj14=True 
                                    if lastl1==True and p1pjcon>0:
                                        if p1pjcon==4:
                                            win.blit(proj11,pjxl11,FIGy1)
                                            p1pjcon-=1
                                            pj11=True
                                        if p1pjcon==3:
                                            win.blit(proj12,pjxl12,FIGy1)
                                            p1pjcon-=1 
                                            pj12=True    
                                        if p1pjcon==2:
                                            win.blit(proj13,pjxl13,FIGy1)
                                            p1pjcon-=1 
                                            pj13=True
                                        if p1pjcon==1:
                                            win.blit(proj14,pjxl14,FIGy1)
                                            p1pjcon-=1 
                                            pj14=True          
                                if spped2==True:
                                    if keyPressed[pygame.K_d]:  
                                        FIGx2 +=speedy 
                                        righ2=True
                                        left2=False
                                        lastr2=True
                                        lastl2=False
                                        lastd2=False
                                        lastw2=False 
                                    if keyPressed[pygame.K_a]:  
                                        FIGx2-=speedy
                                        right2=False
                                        left2=True
                                        lastr2=False
                                        lastl2=True
                                        lastd2=False
                                        lastw2=False
                                    if keyPressed[pygame.K_w]:  
                                        FIGy2-=speedy
                                        lastr2=False
                                        lastl2=False
                                        lastd2=False
                                        lastw2=True
                                    if keyPressed [pygame.K_s]:
                                        FIGy2 +=speedy
                                        lastr2=False
                                        lastl2=False
                                        lastd2=True
                                        lastw2=False
                                if keyPressed[pygame.K_SLASH]:
                                    if lastr2==True and p2pjcon>0:
                                        if p2pjcon==4:
                                            win.blit(proj21,pjxr21,FIGy2)
                                            p2pjcon-=1
                                            pj21=True
                                        if p2pjcon==3:
                                            win.blit(proj22,pjxr22,FIGy2)
                                            p2pjcon-=1 
                                            pj22=True    
                                        if p2pjcon==2:
                                            win.blit(proj23,pjxr23,FIGy2)
                                            p2pjcon-=1 
                                            pj23=True
                                        if p2pjcon==1:
                                            win.blit(proj24,pjxr24,FIGy2)
                                            p2pjcon-=1 
                                            pj24=True
                                    if lastl2==True and p2pjcon>0:
                                        if p2pjcon==4:
                                            win.blit(proj21,pjxr21,FIGy2)
                                            p2pjcon-=1
                                            pj21=True
                                        if p2pjcon==3:
                                            win.blit(proj22,pjxr22,FIGy2)
                                            p2pjcon-=1 
                                            pj22=True    
                                        if p2pjcon==2:
                                            win.blit(proj23,pjxr23,FIGy2)
                                            p2pjcon-=1 
                                            pj23=True
                                        if p2pjcon==1:
                                            win.blit(proj24,pjxr24,FIGy2)
                                            p2pjcon-=1 
                                            pj24=True                        
                                if FIGx1==boldx1+85 or boldx2+85 or boldx3+85 or boldx4+85 or boldx1-85 or boldx2-85 or boldx3-85 or boldx4-85:
                                    spped1=False
                                    pygame.time.delay(3000)
                                    spped1=True
                                if FIGy1==boldy1+85 or boldy2+85 or boldy3+85 or boldy4+85 or boldy1-85 or boldy2-85 or boldy3-85 or boldy4-85:
                                    spped1=False
                                    pygame.time.delay(3000)
                                    spped1=True
                                if FIGx2==boldx1+85 or boldx2+85 or boldx3+85 or boldx4+85 or boldx1-85 or boldx2-85 or boldx3-85 or boldx4-85:
                                    spped1=False
                                    pygame.time.delay(3000)
                                    spped1=True
                                if FIGy2==boldy1+85 or boldy2+85 or boldy3+85 or boldy4+85 or boldy1-85 or boldy2-85 or boldy3-85 or boldy4-85:
                                    spped2=False
                                    pygame.time.delay(3000)
                                    spped2=True
                if xp>x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 7:
                    xp=0
                    yp=0 
                    win.fill(WHITE)
                    display_Title("Testy Game",y)
                    Menu_function(gameMessages,150)
                    counter-=7 
