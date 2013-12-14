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
        
        shipX = .5 * config.SCREEN_X
        shipY = .5 * config.SCREEN_Y
        ShipPos = Point(shipX,shipY)
        self.ship = ship.Ship(ShipPos,config.SHIP_INITIAL_DIRECTION, config.SHIP_COLOR)
        self.shipPos = ShipPos
        self.rocks = []
        totalRocks = config.ROCK_COUNT
        for r in range(totalRocks):
            bRockX = random.randrange(0,config.SCREEN_X)
            bRockY = random.randrange(0, config.SCREEN_Y)
            bRockPos = Point(bRockX,bRockY)
            oddOrEve = random.randrange(-1,2,2)
            rotation = random.uniform(config.ROCK_MIN_ROTATION_SPEED,config.ROCK_MAX_ROTATION_SPEED) * oddOrEve 
            self.bRock = rock.bigRock(bRockPos,random.uniform(0.0,359.99), config.ROCK_COLOR, rotation)
            self.rocks.append(self.bRock)
            self.bRockPos = bRockPos
    def paint(self, surface):
        surface.fill((0,0,0))
        self.ship.paint(surface)
        for r in range(config.ROCK_COUNT):
            self.rocks[r].paint(surface)
       

    def game_logic(self,keys, newkeys):
        self.ship.game_logic(keys, newkeys)
        for r in range(config.ROCK_COUNT):
            self.rocks[r].game_logic(keys, newkeys)
        


def main():
    g = AstroidsGame(config.TITLE, config.SCREEN_X, config.SCREEN_Y,config.FRAMES_PER_SECOND)
    g.main_loop()

main()
