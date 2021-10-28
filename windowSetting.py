#Preston Yoo
#10-28-21
#window ssettings for a game

import pygame, os,random,time

os.system('cls')
pygame.init()
#list fot menu Messages
gameMessages= ["Play Game","Settings","Instructions","Credits"]
settingMessages=["Screen Size","Background Colors", "Object Colors", "Sounds On/Off"]#can use same logic for main menu
#global variables: they work anywhere in the program
colors = {'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,225), 'purple':(150,0,150), 'white':(255,255,255),'black': (0,0,0),'yellow': (255,211,67),'orange':(255, 165, 0), 'black': (0,0,0)}
WHITE=colors.get('white')
BLACK=colors.get('black')
ORANGE=colors.get('orange')

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
    

def Settings_function():
    pygame.time.delay(100)
    ym=y#this works because the other xm is in another function sso it is sepaerate aka a local variable
    xm=x+wbox+10
    for i in range (0,len(settingMessages)):
        word=settingMessages[i]
        pygame.draw.rect(win, ORANGE,square)
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm,ym))
        pygame.display.update()
        pygame.time.delay(100)
        ym+=100
        square.y=ym
def Menu_function():
    pygame.time.delay(100)
    ym=y#this works because the other xm is in another function sso it is sepaerate aka a local variable
    xm=x+wbox+10
    for i in range (0,len(gameMessages)):
        word=gameMessages[i]
        pygame.draw.rect(win, ORANGE,square)
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm,ym))
        pygame.display.update()
        pygame.time.delay(100)
        ym+=100
        square.y=ym
    
display_Title("TestyGame",y)
Menu_function()
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
                if xp >x and xp<x+wbox and yp>y and yp<245:
                    create_NewWindow("Play Game")
                    display_Title("Play Game",40)
                if xp>x and xp<x+wbox and yp>y and yp<345:
                    create_NewWindow("Settings")
                    display_Title("Settings",40)
                    Settings_function()
                if xp>x and xp<x+wbox and yp>y and yp<445:
                    create_NewWindow("Instructions")
                    display_Title("Instructions",40)
                if xp>x and xp<x+wbox and yp>y and yp<545:
                    create_NewWindow("Credits")
                    display_Title("Credits",40)

