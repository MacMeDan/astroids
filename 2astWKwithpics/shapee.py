from point import Point
import config
import random
import math
import pygame




class Shape:
    def __init__(self, position, rotation, color):
    	self.position = position
    	self.rotation = rotation
    	self.color = color
    	self.dx = 0
    	self.dy = 0
    	self.Active = True
    
    def paint(self, surface):
    	NotImplementedError()
    	
    def game_logic(self, keys, newkeys):
    	NotImplementedError()
    
    def move(self):
    	x,y = self.position.pair()
    	x += self.dx
    	y += self.dy
    	self.rotate(self.rotationSpeed)
    	self.position = Point(x,y)
    	if y < -20:						#this makes your ship go completely off screen before wrapping to the other side 
    		y = config.SCREEN_Y +20
    	if x < -20:
    		x = config.SCREEN_X +20
    	if y > config.SCREEN_Y +20:
    		y = -20
    	if x > config.SCREEN_X +20:
    		x = 20
    	self.position = Point(x,y)
    	
    def accelerate(self, acceleration):
    	angleinradians = math.radians(self.rotation)
    	self.dx = self.dx + acceleration * math.cos(angleinradians)
    	self.dy = self.dy + acceleration * math.sin(angleinradians)
    	
    def rotate(self,degrees):
    	self.rotation -= degrees
    	
    def getrotate(self):
    	return self.rotation
    	
    def isActive(self):
    	return self.Active
    
    def setInActive(self):
    	self.Active = False
    	
    def setActive(self):
    	self.Active = True
    	
    def collision(self, notself):
    	x,y = self.position.pair()
    	nx,ny = notself.position.pair()
    	forX = x - nx
    	forY = y - ny
    	if forX < 50 and forX > -50 and forY < 50 and forY > -50:
    		return True
    	else:
    		return False
    	
    		
    def intersect(self, other_polygon):
    	fPoints = self.getPoints()
    	oPoints = other_polygon.getPoints()
    	for p in fPoints:
    		if other_polygon.contains(p):
    			return True
    	for b in self.outline:
    		if self.contains(b):
    			return True
    	else:
    		return False
    		
    def contains(self, point):
    	
    	dist_x = self.position.x - point.x
    	dist_y = self.position.y - point.y
    	return dist_x*dist_x + dist_y*dist_y <= self.radius*self.radius
    	
    def getPoints(self):
    	NotImplementedError()
    	
    def colorz(self):
    	if self.c > 234:
    		self.inc = -1
    	if self.c < 21:
    		self.inc = 1
    	self.c += (config.STAR_TWINKLE_SPEED * self.inc)
    	if self.id == "star":
    		self.color = (self.c,self.c,self.c)
    	