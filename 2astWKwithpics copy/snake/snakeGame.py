import game
import snake
import pygame

class SnakeGame(game.Game):
    def __init__(self):
        game.Game.__init__(self, 'Snake', 640, 480)
        self.snake = snake.Snake(10, (200, 127, 127),640, 480,20)

    def paint(self, surface):
        surface.fill((0,0,0))
        self.snake.paint(surface)

    def game_logic(self,keys, newkeys):
        if pygame.K_UP in newkeys:
            self.snake.up()
        elif pygame.K_DOWN in newkeys:
            self.snake.down()
        elif pygame.K_LEFT in newkeys:
            self.snake.left()
        elif pygame.K_RIGHT in newkeys:
            self.snake.right()
        self.snake.move()
        pass

def main():
    g = SnakeGame()
    g.main_loop()
main()
        
