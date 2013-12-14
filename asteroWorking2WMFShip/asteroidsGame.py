import game
import polygon
import config
import pygame
import ship
import rock
from point import Point
import random


class AstroidsGame(game.Game):
    def __init__(self, name, width, heigth,framerate):
        game.Game.__init__(self,config.TITLE, config.SCREEN_X, config.SCREEN_Y)
        # problems self.surfaceimg = surface.blit(image,(self.ship.position.pair()))
        self.space = []
        self.surfaceing = pygame.image.load("img/mFShip.png").convert_alpha()
        self.ship = ship.Ship(self.surfaceing)
        self.space.append(self.ship)
        for num in range(config.ROCK_COUNT):
            self.bRock = rock.bigRock()
            self.space.append(self.bRock)
            
    def paint(self, surface):
        surface.fill((0,0,0))
        image = pygame.image.load("img/mFShip.png").convert_alpha()
        if self.ship.isActive():
        	self.surfaceing = surface.blit(image,(self.ship.position.pair()))
        for r in self.space[1:]:
        	if r.isActive():
        		r.paint(surface)
       

    def game_logic(self,keys, newkeys):
    	if self.ship.isActive():
    		self.ship.game_logic(keys, newkeys)
    	for r in self.space[1:]:
    		if r.isActive():
    			if self.ship.intersect(r):
    				self.ship.set_inactive()
    		r.game_logic(keys, newkeys)
            


def main():
    g = AstroidsGame(config.TITLE, config.SCREEN_X, config.SCREEN_Y,config.FRAMES_PER_SECOND)
    g.main_loop()

main()
