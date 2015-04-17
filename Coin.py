import pygame, sys, random

class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y): 
		
		super(Coin, self).__init__()
		self.image = pygame.image.load("Coin.png")
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x
