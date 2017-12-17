import math

class Vector():
    
    def __init__(self, direction, length):
        """ 0 -> UP , PI/2 -> RIGHT , PI -> DOWN , PI*3/2 -> LEFT """
        self.dir = direction
        self.len = length
        
    def __add__(self, vector):
        x  = math.sin(self.dir) * self.len + math.sin(vector.dir) * vector.len
        y  = math.cos(self.dir) * self.len + math.cos(vector.dir) * vector.len
        direction  = 0.5 * math.pi - math.atan2(y, x)
        length = math.hypot(x, y)
        return Vector(direction, length)

    def __mul__(self,scalar):
        return Vector(self.dir, self.len * scalar)

    def __truediv__(self,scalar):
        return Vector(self.dir, self.len / scalar)
        
    def add(self, vector):
        x  = math.sin(self.dir) * self.len + math.sin(vector.dir) * vector.len
        y  = math.cos(self.dir) * self.len + math.cos(vector.dir) * vector.len
        self.dir  = 0.5 * math.pi - math.atan2(y, x)
        self.len = math.hypot(x, y)
