import math

class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addVector(self, vector):
        self.x += math.sin(vector.dir) * vector.len
        self.y -= math.cos(vector.dir) * vector.len

    def __setitem__(self, index, value):
        if index == 0 or index == "x":
            self.x = value
        else: self.y = value

    def __getitem__(self, index):
        if index == 0 or index == "x":
            return self.x
        return self.y
