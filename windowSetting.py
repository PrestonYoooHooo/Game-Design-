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

win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Setting Window')
square=pygame.Rect(x,y,wbox,hbox)
#Declare FONTS
TITLE_FONT=pygame.font.SysFont('comicsans',80)
SubTitle=pygame.font.SysFont('comicsnass', 40, italic=True)
MENU_FONT=pygame.font.SysFont('comicsans',40)
text=TITLE_FONT.render('message',1,BLACK)
counter=0
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
                    xp=0
                    yp=0
                    win.fill(WHITE)
                    create_NewWindow("Play Game")
                    display_Title("Play Game",40)
                    Menu_function(PlMessages,150)
                    counter+=7
                    pygame.time.delay(100)
                if xp>x and xp<x+wbox and yp>y and yp<345 and yp>245 and counter is 0:
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
                    HEIGHT=700
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
                if xp>x and xp<x+wbox and yp>y and yp<445 and yp>345 and counter is 7:
                    xp=0
                    yp=0 
                    win.fill(WHITE)
                    display_Title("Testy Game",y)
                    Menu_function(gameMessages,150)
                    counter-=7 