import pygame,sys
from pygame.locals import *
from random import randint
 
pygame.init()
 
#This is the window 
DISPLAY_SURFACE = pygame.display.set_mode((1080,300)) #parameters X,Y in pixels
# CLOCK = pygame.time.Clock()
WHITE = pygame.Color(255,255,255) #instantiates color params: (red:0-255, green:0-255,blue:0-255 )
BLACK = pygame.Color(0,0,0)
RED = pygame.Color(255,0,0)
GREEN=pygame.Color(0,255,0)
BLUE=pygame.Color(0,0,255)
COLORS = [WHITE,BLACK,RED,GREEN, BLUE]
current_color = WHITE
circle_radius = 20
drawing = False
 
 
def randColor()->pygame.Color:
    return pygame.Color(randint(0,255),randint(0,255),randint(0,255))
 
 
sideBar = pygame.Rect(0, 0, 200, 300)
pygame.draw.rect(DISPLAY_SURFACE, WHITE, sideBar)
 
buttonRed = pygame.Rect(50, 50, 100, 75)
pygame.draw.rect(DISPLAY_SURFACE, RED, buttonRed)
 
buttonBlue = pygame.Rect(50, 175, 100, 75)
pygame.draw.rect(DISPLAY_SURFACE, BLUE, buttonBlue)
 
while True: #Game loop
    #mouse coords
    mouse_pos: tuple = pygame.mouse.get_pos() #output -> (x,y)
    pressed_keys:tuple = pygame.key.get_pressed()
    pressed_mouse_buttons:tuple = pygame.mouse.get_pressed()
 
    pygame.display.update() #draws pixels
 
 
 
 
 
    #event commands
    for event in pygame.event.get():
        if event.type == QUIT: #if a QUIT command is sent
            pygame.quit() #the game quits
            sys.exit() 
        # elif event.type == TEXTINPUT:
        #     if pressed_keys[K_r]:
        #         current_color = randColor()
        if not sideBar.collidepoint(mouse_pos):
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                drawing = True
            elif event.type == MOUSEBUTTONUP and event.button==1:
                drawing = False
 
 
        else: 
            drawing = False
            if event.type == MOUSEBUTTONDOWN and event.button==1:
                if buttonRed.collidepoint(event.pos):
                    current_color = RED
                elif buttonBlue.collidepoint(event.pos):
                    current_color = BLUE
                else: current_color = WHITE
 
    if drawing:
        pygame.draw.circle(DISPLAY_SURFACE, current_color, mouse_pos,circle_radius)
 
 
 
    
#TODO
# Scale the marker w arrows
# Have an input box that lets you change the color, preset or custom
# Change the shape on input
# Mouseclick to start and stop the draw
