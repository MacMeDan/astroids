import shapee
import config
import polygon
import random
import math
import circle
import pygame
from point import Point
import ship


class Star(circle.Circle):
    def __init__(self):
    	self.starX = random.randrange(0,config.SCREEN_X)
    	self.starY = random.randrange(0, config.SCREEN_Y)
    	self.position = Point(self.starX,self.starY)
    	self.rotation = 0.0
    	self.c = random.randrange(0, 255)
    	self.color = (self.c,self.c,self.c)
    	self.radius = config.STAR_RADIUS
    	self.tSpeed = config.STAR_TWINKLE_SPEED
    	self.Active = True
    	self.rotation = 0
    	self.id = "star"
    	self.inc = 1
    	self.surface = 0
    	circle.Circle(self.position, self.radius, self.rotation, self.color)
    	
    
    	
    	