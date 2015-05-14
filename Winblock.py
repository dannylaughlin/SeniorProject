import pygame, sys, random

class Winblock(pygame.sprite.Sprite):
 
	def __init__(self, x, y, width, height):
		
		super(Winblock, self).__init__()
 
		self.image = pygame.Surface([width, height])
		self.image.fill((0, 255, 0))
 
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x

		
