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
    	self.color = (random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255))
    	self.radius = config.STAR_RADIUS
    	self.tSpeed = config.STAR_TWINKLE_SPEED
    	self.active =True
    	self.rotation = 0
    	circle.Circle(self.position, self.radius, self.rotation, self.color)
		