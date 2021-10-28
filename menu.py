#Preston Yoo
#10-26-21
#Fontss blit and creating functions
import pygame as py, os, time, random

py.init()
colors = {'red':(150,0,0), 'green':(0,200,0), 'blue': (0,0,225), 'purple':(150,0,150), 'white':(255,255,255),'black': (0,0,0),'yellow': (255,211,67),'orange':(255, 165, 0), 'black': (0,0,0)}
BLACK=colors.get('black')
White=colors.get('white')
objColor=colors.get('red')
width=700
height=700
win=py.display.set_mode((width, height))
win.fill(colors.get('white'))
#results in it being nice and even in the screen
wbox=50#height and width of square
hbox=50
py.font.init #initializes fonts module 
#declare 2 types of fonts ex: title and word
TITLE_FONT=py.font.SysFont('comicsana',80)#make cap to not confuse with variables
WORDS_FONT=py.font.SysFont('comicsana',40)#first name, size, and wiether to bold/italic which are off by defalt
text=TITLE_FONT.render('message',1,colors.get('black'))
def display_Title(message,x,y,):#that comes with def
    py.time.delay(100)
    text=TITLE_FONT.render(message,1,colors.get('black'))#or you can use text but message allows for change
    win.blit(text,(x,y))#the postiion for the text is x,y))#updates pygame for the text
    #the x will be 1/2 of width minus 1/2 of text
    #the y is going to be 1/2 of the height-40 or half the word size
    py.display.update()
    py.time.delay(100)
def display_Words(message,x,y):
    py.time.delay(100)
    text=WORDS_FONT.render('message',1,colors.get('black'))
    win.blit(text,(x,y))
    py.display.update()
    py.time.delay(100)
def wordy ():
    x=width/2-text.get_width()/2-80
    y=height/2-text.get_height()/2-80
    square=py.Rect (x,y,wbox,wbox,)
    xi=width/2-text.get_width()/2-80,
    py.draw.rect(win, objColor,square)
    display_Words("Window Size",width/2-text.get_width()/2,200)
    py.draw.rect(win, objColor,square)
    display_Words("Background Color",width/2-text.get_width()/2,300)
    py.draw.rect(win, objColor,square)
    display_Words("Color",width/2-text.get_width()/2,400)
    py.draw.rect(win, objColor,square)
    display_Words("On/Off Sound",width/2-text.get_width()/2,500)
run=True
while run:
    for eve in py.event.get():
        if eve.type ==py.QUIT:
            run = False
    win.fill(White)
    display_Title("Settings", width/2-text.get_width()/2,40)#the atcual message of function we can change
    py.time.delay(200)
    



