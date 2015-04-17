import pygame, sys, random

class Wall(pygame.sprite.Sprite):
 
	def __init__(self, x, y, width, height, color):
		
		super(Wall, self).__init__()
 
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
 
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x
