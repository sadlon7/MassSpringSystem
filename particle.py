from point import *
from vector import *

class Particle():
    G = 0.1 ## gravity constant
    mass = 1
    elasticity = 0.8
    diameter = 15
    
    def __init__(self, *args):
        """ position is a Point(x,y), velocity a Vector(direction, length) """
        self.position = Point(args[0], args[1])
        self.velocity = Vector(args[2], args[3])
        try:
            self.mass = args[4]
        except :
            pass
        try:
            self.elasticity = args[5]
        except :
            pass
        self.w, self.h = None, None
        self.id = None
        self.color = "white" ##add dependency on density
        self.colorOutline = "teal"
        self.isDragged = False

    def updatePosition(self):
        """ move current particle postion by vector of particle velocity """
        self.position.addVector(self.velocity)

    def applyForce(self, force):
        """ update velocity vector of particle by given force """
        if self.mass:
            self.velocity.add( force / self.mass )
            
    def applyGlobalGravity(self, gravity):
        self.velocity.add( gravity * self.mass )

    def applyParticleAttraction(self, particle):
        """ update velocity vector of self and given particle by dependency of two particles attraction """
        collisionDistance = ( self.diameter + particle.diameter ) / 2
        x,y = self.position.x-particle.position.x, self.position.y-particle.position.y
        distance = math.hypot(x,y)
        
        if distance > collisionDistance :
            force = self.G * self.mass * particle.mass / distance**2 ##Newton's law of universal gravitation
            angle = math.atan2(y,x)  ## headings towards given particle
            self.applyForce( Vector(angle - math.pi/2, force) )
            particle.applyForce( Vector(angle + math.pi/2, force) )

    def checkParticleCollision(self, particle):
        """ prevent overlay of particles by casting collision """
        collisionDistance = ( self.diameter + particle.diameter ) / 2
        x,y = self.position.x-particle.position.x, self.position.y-particle.position.y
        distance = math.hypot( x,y )
        e =self.elasticity * particle.elasticity
        
        if distance <= collisionDistance :
            angle = math.atan2(y,x) + math.pi/2 ##norm of connecion
            mass = self.mass + particle.mass
            tempVel = Vector(self.velocity.dir, self.velocity.len * (self.mass - particle.mass) / mass ) + Vector(angle, 2*particle.velocity.len * particle.mass / mass)
            particle.velocity = Vector(particle.velocity.dir, particle.velocity.len * (particle.mass-self.mass)/mass) + Vector(angle+math.pi, 2*self.velocity.len * self.mass/mass)
            self.velocity = tempVel
            self.velocity *= e
            particle.velocity *= e
            overlay = 0.5*(collisionDistance - distance+1)
            self.position.addVector( Vector(math.sin(angle)*overlay, -math.cos(angle)*overlay) )
            particle.position.addVector( Vector(-math.sin(angle)*overlay, math.cos(angle)*overlay) )
            
    def checkBorderCollision(self):
        """ bound particles in Enviroment and solve its reflection """
        r = self.diameter/2
        w, h = self.w-r, self.h-r
        
        if self.position.x > w:
            self.position.x = w - ( self.position.x - w )
            self.velocity.dir *= -1
            self.velocity *= self.elasticity
            
        elif self.position.x < r:
            self.position.x = 2*r - self.position.x
            self.velocity.dir *= -1
            self.velocity *= self.elasticity
            
        if self.position.y > h:
            self.position.y = h - ( self.position.y - h )
            self.velocity.dir = math.pi - self.velocity.dir
            self.velocity *= self.elasticity
            
        elif self.position.y < r:
            self.position.y = 2*r - self.position.y
            self.velocity.dir = math.pi - self.velocity.dir
            self.velocity *= self.elasticity
            
    def graphicRepr(self, canvas):
        if self.id is None:
            self.createGraphicRepr(canvas)
        else:
            self.updateGraphicRepr(canvas)

    def createGraphicRepr(self, canvas):
        x = self.position.x
        y = self.position.y
        r = self.diameter / 2
        self.id = canvas.create_oval(x-r, y-r, x+r, y+r, fill = self.color, outline = self.colorOutline)

    def updateGraphicRepr(self, canvas):
        x = self.position.x
        y = self.position.y
        r = self.diameter / 2
        canvas.coords( self.id, x-r, y-r, x+r, y+r )
        canvas.itemconfig(self.id, fill = self.color, outline = self.colorOutline)
