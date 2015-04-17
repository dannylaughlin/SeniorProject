import pygame, sys, random
from Ball import *
from Wall import *
from Player import *
from Coin import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
TEAL = (0, 255, 255)


class Room(object):
	wall_list = None
	ball_list = None
	coin_list = None
 
	def __init__(self):
		self.wall_list = pygame.sprite.Group()
		self.ball_list = pygame.sprite.Group()
		self.coin_list = pygame.sprite.Group()
 
 
class Room1(Room):
	def __init__(self):
		Room.__init__(self)
		walls = [[0, 0, 20, 600, WHITE],
				 [780, 0, 20, 250, WHITE],
				 [780, 350, 20, 250, WHITE],
				 [20, 0, 760, 20, WHITE],
				 [20, 580, 760, 20, WHITE],
				 [390, 50, 20, 500, BLUE]
				]
				
		for item in walls:
			wall = Wall(item[0], item[1], item[2], item[3], item[4])
			self.wall_list.add(wall)


class Room2(Room):
	def __init__(self):
		Room.__init__(self)
		
		
		
		walls = [[0, 0, 20, 250, PURPLE],
				 [0, 350, 20, 250, PURPLE],
				 [780, 0, 20, 250, PURPLE],
				 [780, 350, 20, 250, PURPLE],
				 [20, 0, 760, 20, PURPLE],
				 [20, 580, 760, 20, PURPLE]
				]
 
		for item in walls:
			wall = Wall(item[0], item[1], item[2], item[3], item[4])
			self.wall_list.add(wall)
 
		for x in range(100, 800, 100):
			for y in range(50, 451, 300):
				wall = Wall(x, y, 20, 200, TEAL)
				self.wall_list.add(wall)
 
		for x in range(150, 700, 100):
			wall = Wall(x, 200, 20, 200, WHITE)
			self.wall_list.add(wall)
			
		for x in range(152, 702, 100):
			ball = Ball(x, 490, [0,5])
			self.ball_list.add(ball)
			
		for x in range(152, 702, 100):	
			ball = Ball(x, 110, [0,5])
			self.ball_list.add(ball)
		
		for x in range(100, 800, 100):
			ball = Ball(x, 300, [0,5])
			self.ball_list.add(ball)
			
 
class Room3(Room):
	def __init__(self):
		Room.__init__(self)
		
		balls = [
				]
		
		walls = [[0, 0, 20, 250, TEAL],
				 [0, 350, 20, 250, TEAL],
				 [780, 0, 20, 250, TEAL],
				 [780, 350, 20, 250, TEAL],
				 [20, 0, 760, 20, TEAL],
				 [20, 580, 760, 20, TEAL],
				 [190, 50, 20, 500, GREEN],
				 [590, 50, 20, 500, GREEN]
				]
 
		for item in walls:
			wall = Wall(item[0], item[1], item[2], item[3], item[4])
			self.wall_list.add(wall)
			
		for item in balls:
			ball = Ball(item[0], item[1], item[2])
			self.ball_list.add(ball)	
		
		for x in range(273, 530, 50):
			for y in range(180, 421, 20):
				ball = Ball(x, y, [0,5])
				self.ball_list.add(ball)
		
		for x in range(298, 530, 50):
			for y in range(180, 421, 20):
				ball = Ball(x, y, [0,-5])
				self.ball_list.add(ball)
 			
			
class Room4(Room):
	def __init__(self):
		Room.__init__(self)
		
		balls = [
				[400, 20, [5,0]],
				[400, 566, [5,0]],
				
				[400, 283, [5,0]],
				[450, 297, [5,0]],
				[500, 311, [5,0]],
				[550, 325, [5,0]],
				[350, 269, [5,0]],
				[300, 255, [5,0]]
				]
		
		walls = [[0, 0, 20, 250, YELLOW],
				 [0, 350, 20, 250, YELLOW],
				 [780, 0, 20, 250, YELLOW],
				 [780, 350, 20, 250, YELLOW],
				 [20, 0, 760, 20, YELLOW],
				 [20, 580, 760, 20, YELLOW]
				]
 
		for item in walls:
			wall = Wall(item[0], item[1], item[2], item[3], item[4])
			self.wall_list.add(wall)
			
		for item in balls:
			ball = Ball(item[0], item[1], item[2])
			self.ball_list.add(ball)	
 
		for x in range(100, 800, 100):
			for y in range(50, 451, 300):
				wall = Wall(x, y, 20, 200, TEAL)
				self.wall_list.add(wall)
 
		for x in range(150, 700, 500):
			wall = Wall(x, 200, 20, 200, WHITE)
			self.wall_list.add(wall)
		
		
		for x in range(100, 800, 100):
			ball = Ball(x, 300, [0,5])
			self.ball_list.add(ball)
			
		for x in range(100, 800, 200):
			ball = Ball(x, 550, [5,0])
			self.ball_list.add(ball)
		for x in range(100, 800, 200):
			ball = Ball(x, 550, [-5,0])
			self.ball_list.add(ball)	
					
		for x in range(100, 800, 200):
			ball = Ball(x, 35, [5,0])
			self.ball_list.add(ball)
		for x in range(100, 800, 200):
			ball = Ball(x, 35, [-5,0])
			self.ball_list.add(ball)


class Room5(Room):
	def __init__(self):
		Room.__init__(self)
		
		balls = [
				]
		
		walls = [[0, 0, 20, 250, WHITE],
				 [0, 350, 20, 250, WHITE],
				 [780, 0, 20, 600, WHITE],
				 [20, 0, 760, 20, WHITE],
				 [20, 580, 760, 20, WHITE]
				]
 
		for item in walls:
			wall = Wall(item[0], item[1], item[2], item[3], item[4])
			self.wall_list.add(wall)
			
		for item in balls:
			ball = Ball(item[0], item[1], item[2])
			self.ball_list.add(ball)
