import math
import pygame.draw
from point import Point
import config

class Polygon:
    def __init__(self, shape, position, rotation, color, surfaceing):
        self.position = position
        self.rotation = rotation
        self.color = color
        self.active = True
        self.cache_points = (None, None, None)
        self.dx = 0
        self.dy = 0
        self.surfaceing = surfaceing

        # first, we find the shape's top-most left-most boundary, its origin
        (origin_x, origin_y) = (shape[0].x, shape[0].y)
        for p in shape:
            if p.x < origin_x:
                origin_x = p.x
            if p.y < origin_y:
                origin_y = p.y

        # then, we orient all of its points relative to its origin
        shifted = []
        for p in shape:
            shifted.append(Point(p.x - origin_x, p.y - origin_y))

        # now shift them all based on the center of gravity
        self.shape = shifted
        self.center = self._findCenter()
        self.shape = []
        for p in shifted:
            self.shape.append(Point(p.x - self.center.x, p.y - self.center.y))

    # apply the rotation and offset to the shape of the polygon
    def getPoints(self):
        
        (oldrotation, oldposition, oldpoints) = self.cache_points
        
        if oldrotation == self.rotation and oldposition == self.position:
            return oldpoints

        angle = math.radians(self.rotation)
        sin = math.sin(angle)
        cos = math.cos(angle)
        points = []
        for p in self.shape:
            x = p.x * cos - p.y * sin + self.position.x
            y = p.x * sin + p.y * cos + self.position.y
            points.append(Point(x, y))

        self.cache_points = (self.rotation, self.position, points)
        return points

    # test if the given point is inside this polygon
    def contains(self, point):
        points = self.getPoints()
        crossingNumber = 0

        for i in range(len(points)):
            j = (i + 1) % len(points)

            if     (((points[i].x < point.x and point.x <= points[j].x) or
                    (points[j].x < point.x and point.x <= points[i].x)) and
                   (point.y > points[i].y + (points[j].y - points[i].y) /
                    (points[j].x - points[i].x) * (point.x - points[i].x))):
                crossingNumber += 1

        return crossingNumber % 2 == 1
    
    def intersect(self, other_polygon):
    	fPoints = self.getPoints()
    	oPoints = other_polygon.getPoints()
    	for p in fPoints:
    		if other_polygon.contains(p):
    			return True
    	for b in oPoints:
    		if self.contains(b):
    			return True
    	else:
    		return False
    		

    def _findArea(self):
        shape = self.shape
        sum = 0.0

        for i in range(len(shape)):
            j = (i + 1) % len(self.shape)
            sum += shape[i].x * shape[j].y - shape[j].x * shape[i].y
        return abs(0.5 * sum)

    def _findCenter(self):
        shape = self.shape
        (sum_x, sum_y) = (0.0, 0.0)

        for i in range(len(shape)):
            j = (i + 1) % len(self.shape)

            sum_x += (shape[i].x + shape[j].x) * \
                     (shape[i].x * shape[j].y - shape[j].x * shape[i].y)
            sum_y += (shape[i].y + shape[j].y) * \
                     (shape[i].x * shape[j].y - shape[j].x * shape[i].y)

        area = self._findArea()
        return Point(abs(sum_x / (6.0 * area)), abs(sum_y / (6.0 * area)))

    def game_logic(self, keys, newkeys):
        raise NotImplementedError()

    def paint(self, surface):
    	if self.active:
        	points = self.getPoints()
        	self.shape2 =[]
        	for a in points:
        		self.shape2.append(a.pair())
        	pygame.draw.polygon(surface,self.color,self.shape2,0)
        
    def move(self):
    	x,y = self.position.pair()
    	x += self.dx
    	y += self.dy
    	self.rotate(self.rotationSpeed)
    	self.position = Point(x,y)
    	if y < -20:						#this makes your ship go completely off screen before wrapping to the other side 
    		y = config.SCREEN_Y +20
    	if x < -20:
    		x = config.SCREEN_X +20
    	if y > config.SCREEN_Y +20:
    		y = -20
    	if x > config.SCREEN_X +20:
    		x = 20
    	self.position = Point(x,y)
    
    def rotate(self,degrees):
    	pygame.transform.rotate(self.surfaceing, degrees)
    	self.rotation -= degrees
    
    def isActive(self):
    	return self.active
    
    def set_inactive(self):
    	self.active = False