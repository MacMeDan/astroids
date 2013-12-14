import pygame
import random
class Snake:
    def __init__(self, length, color, pixel_width, pixel_height, pixels_per_cell):
        self.width = pixel_width/pixels_per_cell
        self.height = pixel_height/pixels_per_cell
        self.pixels_per_cell = pixels_per_cell
        # how big
        self.length = length
        #color
        self.color = color                 
        # initial direction (up)
        #speed(ignore)
        self.x_rate = 0
        self.y_rate = -1

        #start location
        x = self.width/2
        y = self.height/2

        self.body = []
        for segment in range(self.length):
            self.body.append((x,y))
            y+=1
        
    def paint(self, surface):
        for (x,y) in self.body:
            xpixel = x * self.pixels_per_cell + self.pixels_per_cell/2
            ypixel = y * self.pixels_per_cell + self.pixels_per_cell/2
            rpixel = self.pixels_per_cell/2
            pygame.draw.circle(surface, self.color, (xpixel, ypixel), rpixel)

    def move(self):
        (x,y) = self.body[0]
        x += self.x_rate
        y += self.y_rate
        if y <0:
            y = self.height - 1
        if x<0:
            x = self.width - 1
        if y > self.height - 1:
            y = 0
        if x > self.width - 1:
            x = 0
        
        #test for collision
        collided = False
        for (bx, by) in self.body:
            if x == bx and y == by:
                collided = True

        if collided:
            r = random.randrange(0,255)
            g = random.randrange(0,255)
            b = random.randrange(0,255)
            self.color = (r, g, b)

        self.body.pop()
            
        self.body.insert(0, (x, y))
        
        
       
      

    def up(self):
        self.x_rate = 0
        self.y_rate = -1
    def left(self):
        self.x_rate = -1
        self.y_rate = 0
    def right(self):
        self.x_rate = 1
        self.y_rate = 0
    def down(self):
        self.x_rate = 0
        self.y_rate = 1
        
