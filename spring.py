from particle import *

class Spring:
    DAMPENING = 1
    def __init__(self, restLength, p1, p2):
        self.restLength = math.hypot(p2.position.x - p1.position.x, p2.position.y - p1.position.y)
        self.stiffness  = 1
        self.p1         = p1
        self.p2         = p2
        self.gId        = None

    def update(self):
        #self.doSpringThings()
        self.keepDistance()

    def doSpringThings(self):
        x = self.p2.position.x - self.p1.position.x
        y = self.p2.position.y - self.p1.position.y
        angle = math.atan2(y, x)
        distance = math.hypot(x, y)

        vp1 = Vector(self.p1.position, self.p2.position)
        vp2 = Vector(self.p2.position, self.p1.position)

        np1 = self.normalize(vp1)
        np2 = self.normalize(vp2)
        
        force = Vector(fx, fy)
        self.p1.applyForce( force * self.DAMPENING)
        self.p2.applyForce((force * (-1)) * self.DAMPENING)

    def keepBothDistance(self, distance):
        
        povodnaP1 = Point(self.p1.position.x, self.p1.position.y)
        povodnaP2 = Point(self.p2.position.x, self.p2.position.y)
            
        n1 = self.normalize(Vector(self.p1.position, self.p2.position))
        n2 = self.normalize(Vector(self.p2.position, self.p1.position))
        d = distance - self.restLength
   
        m = self.p2.mass/(self.p1.mass + self.p2.mass)
        dm = d * m
        dmn = n1 * dm
        self.p1.position.addVector(dmn)

        povodnaKnovejp1 = Vector(povodnaP1, self.p1.position)
        self.p1.applyForce(self.normalize(povodnaKnovejp1) * self.p1.mass * povodnaKnovejp1.length())



        _dis = math.hypot(self.p2.position.x - self.p1.position.x, self.p2.position.y - self.p1.position.y)

        #print (self.restLength - distance, math.hypot(dmn.x,dmn.y))
            

        m = self.p1.mass/(self.p1.mass + self.p2.mass)
        dm = d *m
        dmn = n2 * dm
        self.p2.position.addVector(dmn)

        povodnaKnovejp2 = Vector(povodnaP2, self.p2.position)
        self.p2.applyForce(self.normalize(povodnaKnovejp2) * self.p2.mass * povodnaKnovejp2.length())

        #print (self.restLength - distance, math.hypot(dmn.x,dmn.y))
        #print(math.hypot(self.p2.position.x - self.p1.position.x, self.p2.position.y - self.p1.position.y))

    def keepOneDistance(self, distance):
        if self.p1.isDragged:
            dragged = self.p1
            free = self.p2
        else:
            dragged = self.p2
            free = self.p1
        
        povodnaP1 = Point(dragged.position.x, dragged.position.y)
        povodnaP2 = Point(free.position.x, free.position.y)
            
        n1 = self.normalize(Vector(dragged.position, free.position))
        n2 = self.normalize(Vector(free.position, dragged.position))
        d = distance - self.restLength
   
        m = free.mass
        dm = d #* m
        dmn = n2 * dm
        free.position.addVector(dmn)

        povodnaKnovejp1 = Vector(povodnaP2, free.position)
        free.applyForce(self.normalize(povodnaKnovejp1) * free.mass * povodnaKnovejp1.length())

    def keepDistance(self):
        distance = math.hypot(self.p2.position.x - self.p1.position.x, self.p2.position.y - self.p1.position.y)
        if int(distance) != int(self.restLength):
            if self.p1.isDragged is False and self.p2.isDragged is False:
                self.keepBothDistance(distance)
            else:
                self.keepOneDistance(distance,)

            
           
    def draw(self, canvas):
        color = "black"
        x1 = self.p1.position.x
        y1 = self.p1.position.y
        x2 = self.p2.position.x
        y2 = self.p2.position.y

        if self.gId is None:
            self.gId = canvas.create_line(x1, y1, x2, y2, fill = color)
        else:
            canvas.coords(self.gId, x1, y1, x2, y2)

    
            
    def normalize(self, v):
        m = 0.0
        m += v.x ** 2
        m += v.y ** 2
        m  = m ** 0.5
        if m == 0:
            return v
        return Vector(v.x / m, v.y / m)