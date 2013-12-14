import game
import polygon
import config
import pygame
from point import Point
import ship
import bullet
import rock
import random
import star


class AstroidsGame(game.Game):
    def __init__(self, name, width, heigth,framerate):
        game.Game.__init__(self,config.TITLE, config.SCREEN_X, config.SCREEN_Y)
        self.space = []
        self.ship = ship.Ship()
        self.bullets = []
        self.rocks = []
        self.b = 0
        for bu in range(config.BULLET_COUNT):
        	self.bullets.append (bullet.Bullet(Point(self.ship.shipX, self.ship.shipY),self.ship.rotation))
        
        for numb in range(config.STAR_COUNT):
        	self.star = star.Star()
        	self.space.append(self.star)
        
        for num in range(config.ROCK_COUNT):
            self.bRock = rock.bigRock()
            self.rocks.append(self.bRock)
        #self.space.append(self.ship)
            
    def paint(self, surface):
        surface.fill((0,0,0)) 
        for r in self.space:
        	if r.isActive():
        		r.colorz()
        		r.paint(surface)
        locat = self.ship.getPoints()
        x,y = self.ship.position.pair()
        imgp = Point(x -50, y-50)
        imgf = Point(100, 100)
        for f in self.rocks:
        	if f.isActive():
        			surface.blit(f.curImage,(f.position.pair()))
        if self.ship.isActive():
    		surface.blit(self.ship.curImage,(imgp.pair()))
        
       

    def game_logic(self,keys, newkeys):
    	if self.ship.isActive():
    		if pygame.K_SPACE in newkeys:
    			if self.b > config.BULLET_COUNT-1:
    				self.b = 0
    			else:
    				self.space.append(self.bullets[self.b])
    			if self.bullets[self.b].isActive() == False: 
        			self.bullets[self.b].setActive
        			p = []
        			p = self.ship.getPoints()
        			self.bullets[self.b].fire(p[0], self.ship.rotation)
        			self.b += 1
        	for bu in self.bullets:
        		bu.game_logic(keys, newkeys)
    		self.ship.game_logic(keys, newkeys)
    	for ro in self.space[config.STAR_COUNT:config.STAR_COUNT+config.ROCK_COUNT]:
    		if ro.isActive():
    			for v in self.bullets:
    				if ro.intersect(v):
    					ro.set_inactive()
    					v.set_inactive()
    				if self.ship.intersect(ro):
    					self.ship.set_inactive()
    		ro.game_logic(keys, newkeys)
            


def main():
    g = AstroidsGame(config.TITLE, config.SCREEN_X, config.SCREEN_Y,config.FRAMES_PER_SECOND)
    g.main_loop()

main()
