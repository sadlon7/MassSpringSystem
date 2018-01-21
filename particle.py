from point import *


class Particle:

    COLOR      = "gray"
    DIAMETER   = 20
    
    def __init__(self, position, velocity = Vector(0,0), mass = 1, elasticity = 0.8):
        self.position   = position
        self.velocity   = velocity
        self.elasticity = elasticity
        self.force      = Vector(0,0)
        if mass == 0:
            self.mass = 0.0000001
        else:
            self.mass       = mass
        
        
        self.isDragged     = False
        self.gId        = None
        

    def update(self):
        if self.isDragged:
            return
        self.position.addVector(self.velocity)

    def applyForce(self, force):
        if self.mass:
            self.velocity.add( force / self.mass)

    def appplyGlobalGravity(self, gravity):
        if self.mass is 0:
            return
        if round(self.position.y, 1) < 489:
            self.velocity.add(gravity * self.mass)
        else:
            if self.velocity.y  < 0.2 * self.mass:
                self.velocity.y = 0

    def draw(self, canvas):
        if self.gId is None:
            self.createGraphicRepr(canvas)
        else:
            self.updateGraphicRepr(canvas)
            
    def createGraphicRepr(self, canvas):
        x = self.position.x
        y = self.position.y
        r = self.DIAMETER / 2
        self.gId = canvas.create_oval(x - r, y - r, x + r, y + r, fill = self.COLOR, outline = self.COLOR)

    def updateGraphicRepr(self, canvas):
        x = self.position.x
        y = self.position.y
        r = self.DIAMETER / 2
        canvas.coords(self.gId, x - r, y - r, x + r, y + r)
        canvas.itemconfig(self.gId, fill = self.COLOR, outline = self.COLOR)

    def checkBorderCollision(self, w, h):
        r = self.DIAMETER / 2
        w = w - r
        h = h - r

        if self.position.x > w:
            self.position.x     = w - (self.position.x - w)
            self.velocity.x     *= -1
            self.velocity       *= self.elasticity

        elif self.position.x < r:
            self.position.x     = 2 * r - self.position.x
            self.velocity.x     *= -1
            self.velocity       *= self.elasticity

        elif self.position.y > h:
            self.position.y     = h - (self.position.y - h)
            self.velocity.y     *= -1
            self.velocity       *= self.elasticity

        elif self.position.y < r:
            self.position.y     = 2 * r - self.position.y
            self.velocity.y     *= -1
            self.velocity       *= self.elasticity



    def checkParticleCollision(self, particle):

        collDistance = (self.DIAMETER + particle.DIAMETER) / 2
        dx = particle.position.x - self.position.x
        dy = particle.position.y - self.position.y
        r = self.DIAMETER / 2
        distance = math.hypot(dx, dy)

        if distance < collDistance:
            if distance == 0:
                distance = 1

            vp1 = self.velocity.x * dx / distance + self.velocity.y * dy / distance
            vp2 = particle.velocity.x * dx / distance + particle.velocity.y * dy / distance
 
            dt = (self.DIAMETER - distance)/(vp1 - vp2) 
 
            self.position.x     -= self.velocity.x * dt
            self.position.y     -= self.velocity.y * dt
            particle.position.x -= particle.velocity.x * dt
            particle.position.y -= particle.velocity.y * dt
 
            dx = particle.position.x - self.position.x
            dy = particle.position.y - self.position.y
            distance = math.sqrt(dx * dx + dy * dy)

            nx = dx / distance 
            ny = dy / distance
            s = r * 2 - distance

            


            k = -2 *((particle.velocity.x - self.velocity.x) * nx +
                       ( particle.velocity.y - self.velocity.y) * ny) /(1 / self.mass + 1 / particle.mass)

            self.velocity.x = (self.velocity.x - k * nx / self.mass) * self.elasticity
            self.velocity.y = (self.velocity.y - k * ny / self.mass) * self.elasticity
            particle.velocity.x = (particle.velocity.x + k * nx / particle.mass) * particle.elasticity
            particle.velocity.y = (particle.velocity.y + k * ny / particle.mass) * particle.elasticity

            self.position.x     += self.velocity.x * dt
            self.position.y     += self.velocity.y * dt
            particle.position.x += particle.velocity.x * dt
            particle.position.y += particle.velocity.y * dt
           
            return True

        return False
            
            
            

    def normalize(self, v):
        m = 0.0
        m += v.x ** 2
        m += v.y ** 2
        m  = m ** 0.5

        return Vector(self.velocity.x / m, self.velocity.y / m)