import pygame, sys, random

class Ball(pygame.sprite.Sprite):
	
	change_x = 0
	change_y = 0
	
	def __init__(self, x, y, speed = [0,0]): 
 
		super(Ball, self).__init__()
 
		self.image = pygame.image.load("Misc/Ball.png")
		
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.x = x
		self.speed_x = speed[0]
		self.speed_y = speed[1]

		
	
	def move(self, walls):
			
		self.rect.x += self.speed_x
 
		
		block_hit_list = pygame.sprite.spritecollide(self, walls, False)
		for block in block_hit_list:
			
			if self.speed_x > 0:
				self.rect.right = block.rect.left
				self.speed_x = -self.speed_x
			else:

				self.rect.left = block.rect.right
				self.speed_x = -self.speed_x
 
		self.rect.y += self.speed_y
 
		block_hit_list = pygame.sprite.spritecollide(self, walls, False)
		for block in block_hit_list:
 
			if self.speed_y > 0:
				self.rect.bottom = block.rect.top
				self.speed_y = -self.speed_y
			else:
				self.rect.top = block.rect.bottom
				self.speed_y = -self.speed_y
