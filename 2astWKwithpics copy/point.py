class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def pair(self):
        return (int(round(self.x)), int(round(self.y)))

    def __str__(self):
        return 'Point(%.1f, %.1f)' % (self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
