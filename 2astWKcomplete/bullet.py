import shapee
import config
import polygon
import random
import math
import circle
import pygame
from point import Point
import ship


class Bullet(circle.Circle):
    def __init__(self, position, rotation):
    	self.color    = config.BULLET_COLOR
    	self.radius   = config.BULLET_RADIUS
    	self.position = position
    	self.position.x, self.position.x = self.position.pair()
    	circle.Circle(position, self.radius, rotation, self.color)
    	self.active   = False
    	self.rotationSpeed = 0 
    	 
    	
    	
    def game_logic(self, keys, newkeys):
    	if not self.active:
    		return 
    	else:
    		x,y = self.position.pair()
    		if y > config.SCREEN_Y or y < 0 or x > config.SCREEN_X or x < 0:	
    			self.set_inactive()
    		self.move()
    			
    				
    def fire(self, position, rotation):
    	self.setActive()
    	self.position = position
    	self.rotation = rotation
    	self.dx = 0
    	self.dy = 0
    	self.accelerate(config.BULLET_SPEED)
    	
    	
    	