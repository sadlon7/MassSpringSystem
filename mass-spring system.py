#PHYSICAL BASED ANIMATIONS AND MATHEMATICAL MODELLING
#Project: C14: Mass-Spring system (infinity stiff springs)
#Authors: Sadlon, Stachera

from tkinter import *
from space import *
import random

width, height = 600, 400
time = 20

class MassSpringSystem():
    def __init__(self):
        self.time = time
        self.createWindow()
        self.createCanvas()
        self.space = Space(width, height)
        self.running = False
        self.pause = False

    def createWindow(self):
        self.master = Tk()
        self.master.geometry('{}x{}'.format(width + 100 + 15, height + 10 ))
        self.master.resizable(False, False)
        
        bMaster = Frame(self.master)
        bMaster.place(x = width + 5 +5 , y = 125)
        Button(bMaster, text = "Play animation", command = self.run , width = 13).grid(row=0, column=0)
        Button(bMaster, text = "Stop animation", command = self.stop , width = 13).grid(row=1, column=0)
        Button(bMaster, text = "Add particle", command = self.addParticle , width = 13).grid(row=2, column=0)
        Button(bMaster, text = "Add spring", command = self.addSpring , width = 13).grid(row=3, column=0)
        Button(bMaster, text = "Clear all", command = self.clear , width = 13).grid(row=4, column=0)

        self.master.title('C14: Mass-Spring system (infinity stiff springs)   |   Sadlon / Stachera')

    def createCanvas(self):
        self.canvas = Canvas(self.master, width = width, height = height, bd = 0, bg = 'dimgrey')
        self.canvas.place(x = 5, y = 5)

    def addParticle(self):
        self.pause = self.stop()
        dX1 = 200
        dY1 = -90
        dX2 = 450
        dY2 = -175

        master = Toplevel()
        master.geometry('{}x{}'.format(650, 220))
        master.title('Add Particle')
        master.resizable(False, False)
        self.setState(self.master, 'disabled')
        sVars = [StringVar() for i in range(6)]

        ## position ##
        Label(master, text = 'Positoin of particle:').place(x=25, y=5)
        Label(master, text = 'X axis: ').place(x=40, y=30)
        Label(master, text = 'Y axis: ').place(x=40, y=55)
        Entry(master, textvariable = sVars[0], width=7).place(x = 90, y = 30)
        sVars[0].set(str(random.randrange(10,500,15)))     
        Entry(master, textvariable = sVars[1], width=7).place(x = 90, y = 55)
        sVars[1].set(str(30))       

        ## velocity ##
        Label(master, text = 'Velocity of particle:').place(x=25+dX1, y=95+dY1)
        Label(master, text = 'Direction: ').place(x=40+dX1, y=115+dY1)
        Label(master, text = 'Length: ').place(x=40+dX1, y=140+dY1)
        Entry(master, textvariable = sVars[2], width=7).place(x = 120+dX1, y = 115+dY1)
        sVars[2].set(str(0))
        Label(master, text = ' * π').place(x=170+dX1, y=115+dY1)
        Entry(master, textvariable = sVars[3], width=7).place(x = 120+dX1, y = 140+dY1)
        sVars[3].set(str(0)) 

        Label(master, text = 'Behaviour of particle:').place(x=0+dX2, y=180+dY2)
        Label(master, text = 'Mass: ').place(x=25+dX2, y=200+dY2)
        Entry(master, textvariable = sVars[4], width=7).place(x = 90+dX2, y = 200+dY2)
        #sVars[4].set(str(Particle.mass))
        sVars[4].set(str(random.randrange(10,100)/10))

        Label(master, text = 'Elesticity: ').place(x=25+dX2, y=225+dY2)
        Entry(master, textvariable = sVars[5], width=7).place(x = 90+dX2, y = 225+dY2)
        #sVars[5].set(str(Particle.elasticity))
        sVars[5].set(str(random.randrange(3,10)/10))

        Label(master, text = '[Note: Values are generated random by default]').place(x=200, y=100)

        aa = 160
        bb = -100
        
        Button(master, text = "Add",width = 10, command = lambda:self.createParticle(sVars ,master)).place(x=80+aa,y=270+bb)
        Button(master, text = "Cancel",width = 10, command = lambda:self.destroy(master)).place(x=165+aa,y=270+bb)

    def createParticle(self, sVars, widget):
        sVars[2].set(float(sVars[2].get()) * math.pi)
        self.space.addParticle ( Particle(
            *[float(s.get()) for s in sVars]
            ))
        self.destroy(widget)
        self.space.showGraphicRepr(self.canvas)

    def addSpring(self):
        pass

    def setTime(self, t, widget):
        self.time = t
        self.destroy(widget) 
   
    def run(self):
        self.running = True
        self.update()
        
    def stop(self):
        if self.running:
            self.running = False
            return True
        return False
    
    def update(self):
        if self.running: ## main pbd loop
            self.space.update(self.canvas)
            self.canvas.after(self.time, self.update)
            
    def clear(self):
        self.running = False
        self.canvas.delete('all')
        self.space.springs = []
        self.space.particles = []
        self.space.update(self.canvas)

    def setState(self, widget, state='disabled'):
        try:
            widget.configure(state=state)
        except:
            pass
        for child in widget.winfo_children():
            self.setState(child, state=state)

    def destroy(self, widget):
        widget.destroy()
        self.setState(self.master, 'normal')
        if self.pause:
            self.pause = False
            self.run() 

mss = MassSpringSystem()
mainloop()

