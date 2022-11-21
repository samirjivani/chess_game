import pygame
from button import Button
import sys
from chess_gui_two_player import main_gui
from chess_gui_black import main_black
from chess_gui_white import main_white
#from select import Select

display = pygame.display.set_mode((1250,700))
pygame.display.set_caption('start_gui')

start_img = pygame.image.load('start_btn.png').convert_alpha()
start_button = Button(500, 200, start_img, 2)

def Select():
    display2 = pygame.display.set_mode((1250,700))
    pygame.display.set_caption('select_gui')

    single = pygame.image.load('Single_Player.png').convert_alpha()
    single_button = Button(150, 200, single, 0.8)

    multi = pygame.image.load('multiplayer.png').convert_alpha()
    multi_button = Button(700, 220, multi, 0.6)
    run = True
    while run:
        display2.fill((255,255,255))
        
        if single_button.draw(display2):
            
            whiteblack()
        if multi_button.draw(display2):
            main_gui()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run= False
        pygame.display.update()
    pygame.quit()
def whiteblack():
    display3 = pygame.display.set_mode((1250,700))
    pygame.display.set_caption('whiteblack_gui')

    white = pygame.image.load('white.jfif').convert_alpha()
    white_button = Button(150, 200, white, 1.5)

    black = pygame.image.load('black.jfif').convert_alpha()
    black_button = Button(700, 220, black, 2)
    run = True
    while run:
        display3.fill((255,255,255))
        
        if white_button.draw(display3):
            
            main_white()
        elif black_button.draw(display3):
            main_black()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run= False
        pygame.display.update()
    pygame.quit()

run = True
while run:
    display.fill((202,228,242))
    
    if start_button.draw(display):
        Select()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
    pygame.display.update()
pygame.quit()