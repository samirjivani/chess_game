import pygame
import button
import sys

from videoplayer import Video
#create display window

screen2 = pygame.display.set_mode((1250,700))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()


#create button instances

width2  = start_img.get_width()
height2 = start_img.get_height()
print(width2)
print(height2)


#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()#600
		height = image.get_height()#600
        
		self.image = pygame.transform.scale(image, (int((width /2)* scale), int((height/2) * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
start_button = Button(600, 640, start_img, 0.8)
#game loop
def game():
    running = True
    while running:
        screen2.fill((0,0,0))
        
        pygame.display.set_caption('start')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        running = False
        
        pygame.display.update()
        
vid = Video("chess_game.mp4")
vid.set_size((1250, 750))
def intro():
    while True:
        vid.draw(screen2, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                main_game()

def main_game():
	run = True
	while run:

		screen2.fill((202, 228, 241))

		if start_button.draw(screen2):
			game()
		

		#event handler
		for event in pygame.event.get():
			#quit game
			if event.type == pygame.QUIT:
				run = False
				
		pygame.display.update()


intro()
pygame.quit()