import polygon
import config
from point import Point
import pygame

class Ship(polygon.Polygon):
    def __init__(self, position, rotation, color):
        
        pointizzleOfTheRetardedShip = [Point(20,50),Point(40,0),Point(0,0)]
        polygon.Polygon.__init__(self, pointizzleOfTheRetardedShip, position, rotation, color)

    def paint(self, surface):
    
        points = self.getPoints()
        mother =[]
        for a in points:
            mother.append(a.pair())
            
        pygame.draw.polygon(surface,config.SHIP_COLOR,mother,0)

    def move(self):
        x,y = self.position.pair()
        x += 5
        
        if y < -20:						#this makes your ship go completely off screen before wrapping to the other side 
            y = config.SCREEN_Y +20
        if x < -20:
            x = config.SCREEN_X +20
        if y > config.SCREEN_Y +20:
            y = -20
        if x > config.SCREEN_X +20:
            x = 20
        self.position = Point(x,y)


    def game_logic(self, keys, newkeys):
    	x,y = self.position.pair()
    	if pygame.K_UP in keys:
    		self.position = Point(x,y-20)
        if pygame.K_LEFT in keys:
            self.left()
        if pygame.K_RIGHT in keys:
            self.right()
        self.move()

	
	def up(self):#increase acceleration
		pass
    def left(self):
        self.rotation -= 2
    def right(self):
        self.rotation += 2
    def down(self):#decrease acceleration
        pass
        
        
        
        
        
        
        