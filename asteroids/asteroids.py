import game
import polygon
import config
import pygame

 

class AstroidsGame(game.Game):
    def __init__(self, name, width, heigth,framerate):
        game.Game.__init__(self,config.TITLE, config.SCREEN_X, config.SCREEN_Y)
        
        
    def paint(self, surface):
        pass
        

    def game_logic(self,keys, newkeys):
        if pygame.K_UP in newkeys:
            self.Polygon.up()
        elif pygame.K_DOWN in newkeys:
            self.Polygon.down()
        elif pygame.K_LEFT in newkeys:
            self.Polygon.left()
        elif pygame.K_RIGHT in newkeys:
            self.Polygon.right()
        self.polygon.move()
        pass


def main():
    g = AstroidsGame(config.TITLE, config.SCREEN_X, config.SCREEN_Y,config.FRAMES_PER_SECOND)
    g.main_loop()

main()
