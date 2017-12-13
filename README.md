# Mass-Spring system

Projekt na predmet Matematické modelovanie a počítačová animácia fyzikálnych procesov

## Autori

* Martin Sadlon | 1mAIN (m.sadlon93@gmail.com)
* Marek Stachera | 2mAIN (stachera1@uniba.com)

## Poziadavky

Programovacie jazyky a kniznice pouzite v projekte:

* Jazyk: Python 3.6.3
* Kniznice: tkinter

## Popis projektu

* Scene: 2d set of particles interconnected with infinitely stiff (rigid) links (constraints).
* Implement scene definition either read each particle and interconnection (link) data from text file or implement user interface to create particles (position, mass) and links (select 2 particles to create link) by clicking on canvas
* Particles with zero inverse mass (1/mass) should be fixed in space (do not move)
* Implement position based  dynamics algorithm
* Model links as simple distance constraint.
* Particles must collide with ground (bottom of the screen should be rigid ground). Collision constraint simply pushes particle above the ground.
* Gravity acts in negative y-coordinate.
* User should be able to define (change) number iterations of the constraint projection.
* No friction or restitution is needed.
* Add simple damping force to each particle (f = - kd v), where kd is damping coefficient (experiment with it) and v is current velocity of particle.
* Implement user interaction
* Users can click on particles during simulation and drag them
* Rendering – only 2D
* Draw particles as points and links as lines.
