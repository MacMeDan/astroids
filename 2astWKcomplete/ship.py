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
        self.position = Point(self.shipX,self.shipY)
        self.rotationSpeed = 0
        self.outline = [Point(-10,5),Point(-10,-5),Point(10,0)]
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

	
	def up(self):#increase acceleration
		pass
    def left(self):
        self.rotate(config.SHIP_ROTATION_RATE)
    def right(self):
        self.rotate(- config.SHIP_ROTATION_RATE)
    def down(self):#decrease acceleration
        pass

        
        
        
        
        
        