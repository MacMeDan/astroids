import polygon
import config
from point import Point
import pygame
import random
import math


class bod(polygon.Polygon):
	def __init__(self, position, rotation, speed):
		self.position = position
		self.rotationSpeed = 0
		self.body =[]
		self.rotation = rotation
		self.outline = [Point(10,10),Point(100,10),Point(100,40),Point(10,40)]
		self.body.append(pygame.image.load("img/body"+".png").convert_alpha())
		self.id = "rockbod"
		self.curImage  = self.body[0]
		self.bodyShape = polygon.Polygon.__init__(self, self.outline, position, self.rotation*10, (90, 120, 50))
		self.accelerate(speed)
		
	def game_logic(self, keys, newkeys):
		x,y = self.position.pair()
		self.move()
			
			
class lwing(polygon.Polygon):
	def __init__(self, position, rotation, speed):
		x,y = position.pair()
		self.position = Point(x - 30,y)
		self.rotationSpeed = 0
		self.lwing =[]
		self.rotation = rotation
		self.outline  = [Point(10,10),Point(35,10),Point(35,80),Point(10,80)]
		self.lwing.append(pygame.image.load("img/lwing"+".png").convert_alpha())
		self.id = "rocklwing"
		self.curImage = self.lwing[0]
		self.lwShape = polygon.Polygon.__init__(self, self.outline, self.position, self.rotation*10, (69, 20, 150))
		self.accelerate(speed)
	
	def game_logic(self, keys, newkeys):
		x,y = self.position.pair()
		self.move()
		
class rwing(polygon.Polygon):
	def __init__(self, position, rotation, speed):
		x,y = position.pair()
		self.position = Point(x + 40,y)
		self.rotationSpeed = 0
		self.rwing =[]
		self.rotation = rotation
		self.outline  = [Point(10,10),Point(30,10),Point(30,80),Point(10,80)]
		self.rwing.append(pygame.image.load("img/rwing"+".png").convert_alpha())
		self.id = "rockrwing"
		self.curImage = self.rwing[0]
		self.rwShape = polygon.Polygon.__init__(self, self.outline, self.position, self.rotation*10, (64, 20, 50))
		self.accelerate(speed)

	def game_logic(self, keys, newkeys):
		x,y = self.position.pair()
		self.move()
			
class bigRock(polygon.Polygon):
	def __init__(self):
		self.speed    = random.randrange(config.IMFI_MIN_SPEED, config.IMFI_MAX_SPEED)
		self.damage   = 0
		bRockX = random.randrange(0,config.SCREEN_X)
		bRockY = random.randrange(0, config.SCREEN_Y)
		bRockPos = Point(bRockX,bRockY)
		oddOrEve = random.randrange(-1,2,2)
		self.rotationSpeed = random.uniform(config.ROCK_MIN_ROTATION_SPEED,config.ROCK_MAX_ROTATION_SPEED) * oddOrEve 
		self.rotation = random.randrange(0, 36, 10)
		self.rotation = 0
		increment = 0
		self.id = "rock"
		self.outline = [Point(10,10),Point(100,10),Point(100,80),Point(10,80)]
		# while increment < 361:
# 			increment += 360/config.ROCK_POLYGON_SIZE #this makes our rock have a unique shape
# 			radius = random.uniform(config.ROCK_MIN_RADIUS,config.ROCK_MAX_RADIUS)
# 			radianRadius = math.radians(increment)
# 			randPoint = Point(x = math.cos(radianRadius) * radius,y = math.sin(radianRadius) * radius)
# 			self.outline.append(randPoint)
		oddOrEve = random.randrange(-1,2,2)
		randSpeed = random.uniform(config.ROCK_MIN_SPEED,config.ROCK_MAX_SPEED) * oddOrEve
		self.ref = 0
		self.image = []
		for i in range(37):
			self.image.append(pygame.image.load("img/fighter"+str(i)+".png").convert_alpha())
		self.curImage = self.image[-self.rotation]
		polygon.Polygon.__init__(self, self.outline, bRockPos, self.rotation*10, config.ROCK_COLOR)
		self.accelerate(randSpeed)
		self.bod = bod(bRockPos, self.rotation*10,randSpeed)
		self.lwing = lwing(bRockPos, self.rotation*10,randSpeed)
		self.rwing = rwing(bRockPos, self.rotation*10,randSpeed)
		
	def game_logic(self, keys, newkeys):
		x,y = self.position.pair()
		self.move()
		
	def accelerate(self, acceleration):
		angleinradians = math.radians(self.rotation)
		self.dx = self.dx + acceleration * math.cos(angleinradians)
		self.dy = self.dy + acceleration * math.sin(angleinradians)
	
	def randDirection(self,bullet):
		self.body.dx = bullet.dx
		self.body.dy = bullet.dy
		self.lwing.dx = bullet.dy
		self.lwing.dy = bullet.dx
		self.rwing.dx = bullet.dy
		self.rwing.dy = bullet.dx
		
		
		
		
		
		
		
		
		
		
		