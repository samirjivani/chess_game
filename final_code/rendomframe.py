import pygame as py
from button import Button
py.init()
screen2 = py.display.set_mode((1250,700))
py.display.set_caption('Buttons')

p1_img = py.image.load('Single_Player.png').convert_alpha()
p2_img = py.image.load('multiplayer.png').convert_alpha()
w_img = py.image.load('black.jfif').convert_alpha()
b_img = py.image.load('white.jfif').convert_alpha()


p1_button = Button(200, 240, p1_img, 0.8)
p2_button = Button(300,340,p2_img,0.8)
w_button = Button(400,440,w_img,0.8)
b_button = Button(300,340,b_img,0.8)

def main_game():
	run = True
	while run:

		screen2.fill((202, 228, 241))
       
		if p1_button.draw(screen2):
			print("single player")
        
		

		#event handler
		for event in py.event.get():
			#quit game
			if event.type == py.QUIT:
				run = False
				
		py.display.update()



main_game()