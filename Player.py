import pygame, sys, random
from random import randint

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
TEAL = (0, 255, 255)

class Player(pygame.sprite.Sprite):

	change_x = 0
	change_y = 0
 
	def __init__(self, x, y):
		
		super(Player, self).__init__()
		
		self.living = True
		#self.tickDelay = 30
		#self.tick = 30
 
		self.image = pygame.Surface([15, 15])
		self.image.fill((randint(0,255),randint(0,255),randint(0,255)))
 
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x
 
	def changespeed(self, x, y):
		
		self.change_x += x
		self.change_y += y
		
	
	def move(self, walls, balls):
 
		self.rect.x += self.change_x
 
		block_hit_list = pygame.sprite.spritecollide(self, walls, False)
		for block in block_hit_list:
			if self.change_x > 0:
				self.rect.right = block.rect.left
			else:
				self.rect.left = block.rect.right
 
		self.rect.y += self.change_y
 
		block_hit_list = pygame.sprite.spritecollide(self, walls, False)
		for block in block_hit_list:
 
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			else:
				self.rect.top = block.rect.bottom
				
		ball_hit_list = pygame.sprite.spritecollide(self, balls, False)
		for ball in ball_hit_list:
			self.living = False	
