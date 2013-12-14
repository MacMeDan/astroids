import polygon
import config
from point import Point
import pygame
import random
import math

class bigRock(polygon.Polygon):
	def __init__(self):
		bRockX = random.randrange(0,config.SCREEN_X)
		bRockY = random.randrange(0, config.SCREEN_Y)
		bRockPos = Point(bRockX,bRockY)
		oddOrEve = random.randrange(-1,2,2)
		self.rotationSpeed = random.uniform(config.ROCK_MIN_ROTATION_SPEED,config.ROCK_MAX_ROTATION_SPEED) * oddOrEve 
		self.rotation = random.uniform(0.0, 359.99)
		increment = 0
		self.outline = []
		while increment < 361:
			increment += 360/config.ROCK_POLYGON_SIZE #this makes our rock have a unique shape
			radius = random.uniform(config.ROCK_MIN_RADIUS,config.ROCK_MAX_RADIUS)
			radianRadius = math.radians(increment)
			randPoint = Point(x = math.cos(radianRadius) * radius,y = math.sin(radianRadius) * radius)
			self.outline.append(randPoint)
		oddOrEve = random.randrange(-1,2,2)
		randSpeed = random.uniform(config.ROCK_MIN_SPEED,config.ROCK_MAX_SPEED) * oddOrEve
		polygon.Polygon.__init__(self, self.outline, bRockPos, self.rotation, config.ROCK_COLOR)
		self.accelerate(randSpeed)
		
	def game_logic(self, keys, newkeys):
		x,y = self.position.pair()
		self.move()
		
	def accelerate(self, acceleration):
		angleinradians = math.radians(self.rotation)
		self.dx = self.dx + acceleration * math.cos(angleinradians)
		self.dy = self.dy + acceleration * math.sin(angleinradians)