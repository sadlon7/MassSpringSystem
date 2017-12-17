from particle import *

class Space():
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.gravitation = Vector(math.pi, 0.05)    
        self.particles = []
        self.canvas = None

    def addParticle(self, particle):
        particle.w, particle.h = self.width, self.height
        self.particles.append(particle)

    def addSpring(self, spring):
        self.springs.append(spring)

    def showGraphicRepr(self, canvas):
        for p in self.particles:
            p.graphicRepr( canvas )

    def update(self, canvas):
        for i,p in enumerate(self.particles):
            p.applyGlobalGravity( self.gravitation )
            for p2 in self.particles[i+1:]:
                p.checkParticleCollision(p2)
            if not p.isDragged:
                p.updatePosition()
            p.checkBorderCollision()
        self.showGraphicRepr(canvas)
