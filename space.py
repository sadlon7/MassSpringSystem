from spring import *
from tkinter import *

class Space:

    def __init__(self, w, h):
        self.width      = w
        self.height     = h
        self.gravity    = Vector(0, 0.05)

        self.particles  = []
        self.springs    = []

    def addParticle(self, particle):
        self.particles.append(particle)

    def addSpring(self, spring):
        self.springs.append(spring)

    def findParticle(self, x, y, rc = 1):
        for i,p in enumerate(self.particles):
            if math.hypot(p.position.x - x, p.position.y - y) <= p.DIAMETER/2 * rc:
                return i
        return None

    def draw(self, canvas):
        for p in self.particles:
            p.draw(canvas)
        for s in self.springs:
            s.draw(canvas)

    def update(self, canvas):        
        for i,p in enumerate(self.particles):
            p.appplyGlobalGravity(self.gravity)
            p.update()
            for p2 in self.particles[i + 1:]:
                p.checkParticleCollision(p2)          
            p.checkBorderCollision(self.width, self.height)
        for s in self.springs:
            s.update()
            s.p1.checkBorderCollision(self.width, self.height)
            s.p2.checkBorderCollision(self.width, self.height)
            for p in self.particles:
                if p != s.p1:
                    s.p1.checkParticleCollision(p)
                if p != s.p2:
                    s.p2.checkParticleCollision(p)

        self.draw(canvas)
'''
canvas = Canvas(width = 500, height = 500, bd = 0, bg = 'white')
canvas.place(x = 5, y = 5)

s = Space(500, 500)
p1 = Particle(Point(100,150) ,Vector(0, 0), 30)
p2 = Particle(Point(100, 270), Vector(-5, 2), 1)
p3 = Particle(Point(250,250), Vector(0,2), 60)
p4 = Particle(Point(400,50), Vector(5,2))

s.addParticle( p1)
s.addParticle( p2)
s.addParticle(p3)
s.addParticle(p4)
s.addSpring(Spring(100,  p1, p2))
s.addSpring(Spring(150,  p2, p3))
s.addSpring(Spring(150,  p3, p4))

#s.addSpring
#s.addParticle( Particle(Point(196,400), Vector(0,2)))
#s.addParticle( Particle(Point(100,300), Vector(2,4)))
#s.addParticle( Particle(Point(170,400), Vector(3,1)))
#s.addParticle( Particle(Point(30,100), Vector(2,0)))
#s.addParticle( Particle(Point(3000,30), Vector(3,0)))

def update():
    s.update(canvas)
    canvas.after(20, update)

update()

canvas.pack()
mainloop()
'''