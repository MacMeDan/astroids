import polygon
import config
from point import Point
import pygame
import random

class bigRock(polygon.Polygon):
	def __init__(self, position, rotation, color, rotationSpeed):
		self.rotationSpeed = rotationSpeed
		config.ROCK_POLYGON_SIZE
		makeARock = [Point(0,0),Point(10,7),Point(0,20),Point(20,10),Point(30,20),Point(30,10),Point(30,-5),Point(50,-5),Point(20,-15),Point(20,-10)]
		polygon.Polygon.__init__(self, makeARock, position, rotation, color)

	def paint(self, surface):
		points = self.getPoints()
		ridges = []
		for a in points:
			ridges.append(a.pair())
			
		pygame.draw.polygon(surface,config.ROCK_COLOR,ridges,0)
	
	def move(self):
		x,y = self.position.pair()
		x -= 5
		self.rotate(self.rotationSpeed)
		if y < 0:
			y = config.SCREEN_Y - 1
		if x < 0:
			x = config.SCREEN_X - 1
		if y > config.SCREEN_Y - 1:
			y = 0
		if x > config.SCREEN_X - 1:
			x = 0
		self.position = Point(x,y)
		
	def rotate(self,degrees):
		self.rotation -= degrees
		
	def game_logic(self, keys, newkeys):
		x,y = self.position.pair()
		self.move()