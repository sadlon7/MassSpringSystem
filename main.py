from space import *
from tkinter import  *
from random import *


class Main:

    TIME    = 20
    WIDTH   = 800
    HEIGHT  = 500
    def __init__(self):
        self.createWindow()
        self.createCanvas()
        self.space = Space(self.WIDTH, self.HEIGHT)

        self.B1Down         = False
        self.stChoosen      = None
        self.ndChoosen      = None
        self.dragParticle   = None

        self.running    = False
        self.pause      = False

        self.clickOutCount  = 0
        
        self.iteration      = 0
        

    def createWindow(self):
        self.master = Tk()
        self.master.geometry('{}x{}'.format(self.WIDTH + 100 + 30, self.HEIGHT + 10))
        self.master.resizable(False, False)

        menubar1 = Menu(self.master)
        menubar2 = Menu(self.master)
        manubar3 = Menu(self.master)

       
        #Buttons--------------------------

        bMaster = Frame(self.master)
        bMaster.place(x = self.WIDTH + 5, y = 5)
        btnWidth = 15
        Button(bMaster, text = "Run", command = self.run, width = btnWidth).grid(row = 0, column = 0)
        Button(bMaster, text = "Stop", command = self.stop, width = btnWidth).grid(row = 1, column = 0)
        Button(bMaster, text = "Add particle", command = self.addParticle, width = btnWidth).grid(row = 3, column = 0)
        Button(bMaster, text = "Add spring", command = self.addSpring, width = btnWidth).grid(row = 4, column = 0)
        Button(bMaster, text = "Clear", command = self.clear, width = btnWidth).grid(row = 5, column = 0)
                
        Label(bMaster, text = "  Iterations: \n (0 = infinity iterations").grid(row = 6, column = 0)
        self.varIterations  = Entry(bMaster, width = 5)
        self.varIterations.grid(row = 7, column = 0)
        self.varIterations.insert(0,str(0))

        self.master.title('Mass-Spring system (infinit stiff springs) - Sadloň, Stachera')
        self.master.config(menu = menubar1)

    def createCanvas(self):
        self.canvas = Canvas(self.master, width = self.WIDTH, height = self.HEIGHT, bd = 0, bg = "white")
        self.canvas.place(x = 5, y = 5)
        self.canvas.bind('<Button-1>', self.click)
        self.canvas.bind('<B1-Motion>', self.drag)
        self.canvas.bind('<ButtonRelease-1>', self.release)

    
    def addParticle(self):
        self.pause = self.stop()

        self.setState(self.master, 'disabled')
        sVars = [StringVar() for i in range(6)]

        master = Toplevel()
        master.geometry('{}x{}'.format(450,100))
        master.title('Add particle')
        master.resizable(False, False)

        #position-------------------------------
        Label(master, text = 'Position:').place(x = 30, y = 10)
        Label(master, text = 'x: ').place(x = 30, y = 30)
        Label(master, text = 'y: ').place(x = 30, y = 55)
        Entry(master, textvariable = sVars[0], width = 5).place(x = 60, y = 30)
        Entry(master, textvariable = sVars[1], width = 5).place(x = 60, y = 55)

        sVars[0].set(str(randrange(25, self.WIDTH - 25, 15)))
        sVars[1].set(str(30))

        #velocity-------------------------------
        Label(master, text = 'Velocity:').place(x = 130, y = 10)
        Label(master, text = 'x: ').place(x = 130, y = 30)
        Label(master, text = 'y: ').place(x = 130, y = 55)
        Entry(master, textvariable = sVars[2], width = 5).place(x = 160, y = 30)
        Entry(master, textvariable = sVars[3], width = 5).place(x = 160, y = 55)

        sVars[2].set(str(0))
        sVars[3].set(str(0))

        #mass-----------------------------------
        Label(master, text = 'Mass: ').place(x = 230, y = 30)
        Entry(master, textvariable = sVars[4], width = 5).place(x = 270, y = 30)
        sVars[4].set(str(1))

        #elasticity-----------------------------------
        Label(master, text = 'Elasticity: ').place(x = 330, y = 30)
        Entry(master, textvariable = sVars[5], width = 5).place(x = 390, y = 30)
        sVars[5].set(str(0.8))

        Button(master, text = "Add", width = 10, command = lambda:self.createParticle(sVars, master)).place(x=250,y=70)
        Button(master, text = "Cancel", width = 10, command = lambda:self.destroy(master)).place(x=350,y=70)

    
    def addSpring(self):
        self.pause = self.stop()
        self.setState(self.master, 'disabled')

        master = Toplevel()
        master.geometry('{}x{}'.format(300,100))
        master.title('Add spring')
        master.resizable(False, False)

        if self.stChoosen is not None and self.ndChoosen is not None:
            Label(master, text = 'Do you really want to add spring ?').place( x = 75, y = 25)
            Button(master, text = "Yes",width = 10, command = lambda:self.createSpring(master)).place(x=35,y=70)
            Button(master, text = "No",width = 10, command = lambda:self.destroy(master)).place(x=185,y=70)

        else:
            Label(master, text = 'First select two particle, by clicking them.').place(x=8, y=25)
            Button(master, text = "ok",width = 10, command = lambda:self.destroy(master)).place(x=85,y=70)
        


    def createSpring(self, widget):
        self.space.addSpring(
            Spring(0, self.stChoosen, self.ndChoosen)
            )
        self.destroy(widget)
        self.space.draw(self.canvas)


    def createParticle(self, sVars, widget):

        self.space.addParticle( Particle(Point(float(sVars[0].get()), float(sVars[1].get())), Vector(float(sVars[2].get()), float(sVars[3].get())),
                                        float(sVars[4].get()), float(sVars[5].get())))
        self.destroy(widget)
        self.space.draw(self.canvas)

    def loadFile(self):
        ...

    def close(self):
        ...

    def defaults(self):
        ...

    def iteration(self):
        ...
      
    def run(self):
        self.running = True
        self.varIterations.config(state = 'disabled')
        self.update()

    def update(self):
        if self.iteration >= int(self.varIterations.get()) and int(self.varIterations.get()) != 0:
            self.stop()
        if self.running:
            self.space.update(self.canvas)
            self.iteration += 1
            self.canvas.after(self.TIME, self.update)



    def stop(self):
        if self.running:
            self.running = False
            self.varIterations.config(state = 'normal')
            self.iteration = 0
            return True
        return False

    def clear(self):
        self.stop()
        self.stChoosen = None
        self.ndChoosen = None
        self.canvas.delete('all')
        self.space.springs = []
        self.space.particles = []
        self.space.update(self.canvas)

    def click(self, e):
        self.B1Down = True
        choosen = self.space.findParticle(e.x, e.y , 2)
        if choosen is not None:
            self.dragParticle = self.space.particles[choosen] ## drag
            self.clickOutCount = 0
            if self.stChoosen is None:
                self.stChoosen = self.space.particles[choosen]
                self.stChoosen.COLOR = 'red'

            if self.space.particles[choosen] is not self.stChoosen and self.space.particles[choosen] is not self.ndChoosen:
                if self.ndChoosen is not None:
                    self.stChoosen.COLOR = 'gray'
                    self.stChoosen = self.ndChoosen
                self.ndChoosen = self.space.particles[choosen]
                self.ndChoosen.COLOR = 'red'
                
            self.space.draw(self.canvas)
        if choosen is None and self.stChoosen is not None:
            self.clickOutCount += 1

        if  self.clickOutCount > 1 :
            if self.stChoosen is not None:
                self.stChoosen.COLOR = 'gray'
            if self.ndChoosen is not None:
                self.ndChoosen.COLOR = 'gray'
            self.stChoosen, self.ndChoosen = None, None
            self.clickOutCount = 0
            self.space.draw(self.canvas)

    def drag(self, e):
        if self.running is False:
            return
        if self.dragParticle is not None:
            self.dragParticle.isDragged = True
            x = e.x -  self.dragParticle.position.x
            y = e.y -  self.dragParticle.position.y
            self.dragParticle.position.x = e.x
            self.dragParticle.position.y = e.y

    def release(self, e):
        if self.dragParticle is not None:
            self.dragParticle.isDragged = False
            self.dragParticle.velocity = Vector(0,0)
            self.dragParticle = None

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

a = Main()
mainloop()