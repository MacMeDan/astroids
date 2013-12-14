class Shape:
    def __init__(self, position, rotation, color):
    	self.dx = 0
    	self.dy = 0
    
    def paint(self, surface):
    	NotImplementedError()
    	
    def game_logic(self, keys, newkeys):
    	NotImplementedError()
    
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
    	
    def accelerate(self, acceleration):
    	angleinradians = math.radians(self.rotation)
    	self.dx = self.dx + acceleration * math.cos(angleinradians)
    	self.dy = self.dy + acceleration * math.sin(angleinradians)