from vector import *

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addVector(self, vector):
        self.x += vector.x
        self.y += vector.y

    def __mul__(self,scalar):
        return Point(self.x * scalar, self.y * scalar)