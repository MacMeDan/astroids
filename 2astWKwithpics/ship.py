import polygon
import bullet
import config
import math
from point import Point
import pygame


class Ship(polygon.Polygon):
    def __init__(self):
        self.shipX = .5 * config.SCREEN_X
        self.shipY = .5 * config.SCREEN_Y
        self.mfx = .5 * config.SCREEN_X
        self.mfy = .5 * config.SCREEN_Y
        self.position = Point(self.shipX,self.shipY)
        self.imPos = Point(self.mfx,self.mfy)
        self.rotationSpeed = 0
        self.outline = [Point(100,100),Point(100,85),Point(60,65),Point(40,65),Point(20,85),Point(20,100),Point(40,120),Point(60,120)]
        self.ref = 0
        self.id = "ship"
        self.image = []
        for i in range(37):
        	self.image.append(pygame.image.load("img/mFShip"+str(i)+".png").convert_alpha())
		
        self.curImage = self.image[self.ref]
        polygon.Polygon.__init__(self, self.outline, self.position, config.SHIP_INITIAL_DIRECTION, config.SHIP_COLOR)
    

    def game_logic(self, keys, newkeys):
    	x,y = self.position.pair()
    	
    	
    	if pygame.K_UP in keys:
    		self.accelerate(config.SHIP_ACCELERATION_RATE)
        if pygame.K_LEFT in keys:
            self.left()
        if pygame.K_RIGHT in keys:
            self.right()
        if pygame.K_DOWN in keys:
            self.accelerate(- config.SHIP_ACCELERATION_RATE)
        self.move()

	
    def left(self):
        self.rotate(config.SHIP_ROTATION_RATE)
        if self.ref == 36:
    		self.ref = 0
    	self.ref += 1
        self.curImage = self.image[self.ref]
    def right(self):
    	if self.ref == 0:
    		self.ref = 36
        self.rotate(- config.SHIP_ROTATION_RATE)
        self.ref -= 1
        self.curImage = self.image[self.ref]

        
        
        
        
        
        