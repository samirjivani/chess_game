import pygame
from button import Button
import sys
from chess_gui import main_gui
def Select():
    display2 = pygame.display.set_mode((1250,700))
    pygame.display.set_caption('select_gui')

    single = pygame.image.load('Single_Player.png').convert_alpha()
    single_button = Button(150, 200, single, 0.8)

    multi = pygame.image.load('multiplayer.png').convert_alpha()
    multi_button = Button(700, 200, multi, 0.8)
    run = True
    while run:
        display2.fill((255,255,255))
        
        if single_button.draw(display2):
            
            print("single")
        elif multi_button.draw(display2):
            main_gui()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run= False
        pygame.display.update()
    pygame.quit()
