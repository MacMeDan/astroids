import shapee
import config
import random
import math
import pygame
from point import Point


class Circle(shapee.Shape):
    def __init__(self, position, radius, rotation, color):
    	shapee.Shape.__init__(self, position, rotation, color)
    	self.active = False
    	self.position = position
    	self.radius = radius
    	self.rotation = rotation
    	self.color = color
    	increment = 0
    	outline = []
    	while increment < 361:
			increment += 360/config.BULLET_POINT_COUNT #this makes our rock have a unique shape
			radianRadius = math.radians(increment)
			randPoint = Point(x = math.cos(radianRadius) * radius,y = math.sin(radianRadius) * radius)
			outline.append(randPoint)
			
	
    	
    
    def paint(self, surface):
    	if self.active: 
        	pygame.draw.circle(surface, self.color, self.position.pair(), int(self.radius), 0)
        	
        	
    	
    def isActive(self):
    	return self.active
    
    def set_inactive(self):
    	self.active = False