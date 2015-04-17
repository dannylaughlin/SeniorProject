import pygame, sys, random, winsound
from random import randint
from HUD import Score
from HUD import Text
from Rooms import *
from Ball import *
from Wall import *
from Player import *
from Coin import *
from Button import Button


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
TEAL = (0, 255, 255)			



 
def main():
 
	pygame.init()
 
	screen = pygame.display.set_mode([800, 600])
 
	pygame.display.set_caption('Dodge The Balls')
 
	player = Player(50, 50)
	movingsprites = pygame.sprite.Group()
	movingsprites.add(player)
 
	rooms = []
 
	room = Room1()
	rooms.append(room)
 
	room = Room2()
	rooms.append(room)
 
	room = Room3()
	rooms.append(room)
	
	room = Room4()
	rooms.append(room)
	
	room = Room5()
	rooms.append(room)
 
	current_room_no = 0
	current_room = rooms[current_room_no]
 
	clock = pygame.time.Clock()
	
	
	win = False
	play = False
	die = False
	
	
	bgColor = r,g,b = 100, 255, 80
	bgImage = pygame.image.load("Screens/New Screen.png").convert()
	bgRect = bgImage.get_rect()
	
	startButton = Button([400, 400], 
					 "Buttons/Start Base.png", 
					 "Buttons/Start Clicked.png")
	
	
	pygame.mixer.init()
	music = pygame.mixer.Sound("Lavender Remix (Normal Speed).wav")
	
	while not play and not win:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					play = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				startButton.click(event.pos)
			if event.type == pygame.MOUSEBUTTONUP:
				if startButton.release(event.pos):
					play = True
		
		
		
		bgColor = r,g,b
		screen.fill(bgColor)
		screen.blit(bgImage, bgRect)
		screen.blit(startButton.image, startButton.rect)
		pygame.display.flip()
		clock.tick(60)
		
	while play and not win:
 
		# --- Event Processing ---
 
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					player.changespeed(-5, 0)
				if event.key == pygame.K_RIGHT:
					player.changespeed(5, 0)
				if event.key == pygame.K_UP:
					player.changespeed(0, -5)
				if event.key == pygame.K_DOWN:
					player.changespeed(0, 5)
 
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					player.changespeed(5, 0)
				if event.key == pygame.K_RIGHT:
					player.changespeed(-5, 0)
				if event.key == pygame.K_UP:
					player.changespeed(0, 5)
				if event.key == pygame.K_DOWN:
					player.changespeed(0, -5)
 
		# --- Game Logic ---
 
		player.move(current_room.wall_list, current_room.ball_list)
		for ball in current_room.ball_list:
			ball.move(current_room.wall_list)
		
		player.image.fill((randint(0,255),randint(0,255),randint(0,255)))
		
		if player.rect.x < -13:
			if current_room_no == 0:
				current_room_no = 0
				current_room = rooms[current_room_no]
				player.rect.x = 790
			elif current_room_no == 2:
				current_room_no = 1
				current_room = rooms[current_room_no]
				player.rect.x = 790
			elif current_room_no == 3:
				current_room_no = 2
				current_room = rooms[current_room_no]
				player.rect.x = 790
			elif current_room_no == 4:
				current_room_no = 3
				current_room = rooms[current_room_no]
				player.rect.x = 790
			else:
				current_room_no = 0
				current_room = rooms[current_room_no]
				player.rect.x = 790
 
		if player.rect.x > 799:
			if current_room_no == 0:
				current_room_no = 1
				current_room = rooms[current_room_no]
				player.rect.x = 0
			elif current_room_no == 1:
				current_room_no = 2
				current_room = rooms[current_room_no]
				player.rect.x = 0
			elif current_room_no == 2:
				current_room_no = 3
				current_room = rooms[current_room_no]
				player.rect.x = 0
			elif current_room_no == 3:
				current_room_no = 4
				current_room = rooms[current_room_no]
				player.rect.x = 0
				die = True
			else:
				current_room_no = 1
				current_room = rooms[current_room_no]
				player.rect.x = 0
		
		
		if player.living == False:
			player.rect.x = 50
			player.rect.y = 300
			player.living = True
	 
		
		# --- Music ---
		
		
		
		# --- Drawing ---
		screen.fill(BLACK)
		
		movingsprites.draw(screen)
		current_room.wall_list.draw(screen)
		current_room.ball_list.draw(screen)
		pygame.display.flip()
 
		clock.tick(60)
		
		#music.play()
	
		

 
if __name__ == "__main__":
	main()
