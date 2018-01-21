import math
import point

class Vector():
    def __init__(self, x, y):
        try:
            self.x = y.x - x.x
            self.y = y.y - x.y
        except:
            self.x = x
            self.y = y

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)


    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self,scalar):
        return Vector(self.x / scalar, self.y / scalar)
        
    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def length(self):
        return math.hypot(self.x, self.y)


    def multiply(self, vector):
        return Vector(self.x * vector.x, self.y * vector.y)

    def dotProduct(self, v):
        r = 0.0
        r += self.x * v.x
        r += self.y * v.y
        return r





    
        
