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
        self.space   = []
        self.ship    = ship.Ship()
        self.bullets = []
        self.rocks   = []
        self.bfighter= []
        self.b       = 0
        
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
        for k in self.rocks:
        	k.paint(surface)
        	k.bod.paint(surface)
        	k.lwing.paint(surface)
        	k.rwing.paint(surface)
        for r in self.space:
        	if r.isActive():
        		r.colorz()
        		r.paint(surface)
        locat = self.ship.getPoints()
        x,y = self.ship.position.pair()
        imgp = Point(x - 50, y - 50)
        for f in self.rocks:
        	rx,ry = f.position.pair()
        	impF = Point(rx - 50, ry - 50)
        	mx,my = f.bod.position.pair()
        	impm = Point(mx - 50, my - 50)
        	lx,ly = f.lwing.position.pair()
        	limpm = Point(lx - 50, ly - 50)
        	tx,ty = f.rwing.position.pair()
        	timpm = Point(tx - 50, ty - 50)
        	if f.isActive():
        		surface.blit(f.curImage,(impF.pair()))
        	if f.bod.isActive():
        		surface.blit(f.bod.curImage,(impm.pair()))
        	if f.lwing.isActive():
        		surface.blit(f.lwing.curImage,(limpm.pair()))
        	if f.rwing.isActive():
        		surface.blit(f.rwing.curImage,(timpm.pair()))
        if self.ship.isActive():
        	surface.blit(self.ship.curImage,(imgp.pair()))
        
       

    def game_logic(self,keys, newkeys):
    	if pygame.K_n in newkeys:
    		self.ship.setActive()
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
    	for ro in self.rocks:
    		for w in self.bullets:
				if ro.isActive() == False:
					if ro.bod.collision(w):
						ro.bod.setInActive
					elif self.ship.collision(ro.bod):
						self.ship.setInActive()
					if ro.lwing.collision(w):
						ro.lwing.setInActive
					elif self.ship.collision(ro.lwing):
						self.ship.setInActive()
					if ro.rwing.collision(w):
						ro.bod.setInActive
					elif self.ship.collision(ro.rwing):
						self.ship.setInActive()
				
    		if ro.isActive():
    			if self.ship.collision(ro):
    				self.ship.setInActive()
    			for v in self.bullets:
    				if v.isActive():
	    				if ro.collision(v):
							ro.setInActive()
							v.setInActive()
							ro.bod.dx = v.dx
							ro.bod.dy = v.dy
							ro.lwing.dx = -v.dy
							ro.lwing.dy = v.dy
							ro.rwing.dx = v.dx
							ro.rwing.dy = v.dx
							return
    		ro.game_logic(keys, newkeys)
    		ro.bod.game_logic(keys, newkeys)
    		ro.lwing.game_logic(keys, newkeys)
    		ro.rwing.game_logic(keys, newkeys)
    		
            


def main():
    g = AstroidsGame(config.TITLE, config.SCREEN_X, config.SCREEN_Y,config.FRAMES_PER_SECOND)
    g.main_loop()

main()
