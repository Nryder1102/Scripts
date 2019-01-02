from graphics import *
from math import *
from random import *
def main():
    win = GraphWin("Test", 1000, 1000)
    win.setCoords(-500.0, -500.0, 500.0, 500.0)
    win.setBackground("black")
    shapeleft = Polygon(Point(0,50), Point(0,-50), Point(-75,0))
    shapeleft.setOutline("dark red")
    shapeleft.setFill("red")
    shapeup = Polygon(Point(50,0), Point(-50,0), Point(0, 75))
    shapeup.setOutline("sky blue")
    shapeup.setFill("light blue")
    shaperight = Polygon(Point(0,-50), Point(0,50), Point(75,0))
    shaperight.setOutline("red")
    shaperight.setFill("dark red")
    shapedown = Polygon(Point(50,0), Point(-50,0), Point(0, -75))
    shapedown.setOutline("light blue")
    shapedown.setFill("sky blue")
    t = Text(Point(0,75), "Press 'Enter' to start!")
    ttwo = Text(Point(0,55), "Use 'Up' 'Down' 'Left' 'Right' to control!")
    tthree = Text(Point(0, 35), "Use 'ESC' to quit!")
    tfour = Text(Point(0,55), "Game Over!!")
    t.setTextColor("white")
    ttwo.setTextColor("white")
    tthree.setTextColor("white")
    tfour.setTextColor("red")
    t.draw(win)
    ttwo.draw(win)
    tthree.draw(win)
    turns = 0
    enemy1 = Circle(Point(-500, 0), 25)
    enemy1.setFill("dark gray")
    enemy1.setOutline("white")
    enemy1.setWidth(5)
    enemy1state = 15
    e1drawstate = 0
    buffer = 0
    key = win.getKey()
    if key == "Return":
        t.undraw()
        ttwo.undraw()
        tthree.undraw()
        while key != "Escape":
            key = win.getKey()
            if key == "Up":
                shapeup.undraw()
                shapeleft.undraw()
                shaperight.undraw()
                shapedown.undraw()
                shapeup.draw(win)
                shapestate = "shapeup.draw(win)"
            elif key == "Right":
                shaperight.undraw()
                shapeleft.undraw()
                shapedown.undraw()
                shapeup.undraw()
                shaperight.draw(win)
                shapestate = "shaperight.draw(win)"
            elif key == "Down":
                shapedown.undraw()
                shapeleft.undraw()
                shaperight.undraw()
                shapeup.undraw()
                shapedown.draw(win)
                shapestate = "shapedown.draw(win)"
            elif key == "Left":
                shapeleft.undraw()
                shaperight.undraw()
                shapedown.undraw()
                shapeup.undraw()
                shapeleft.draw(win)
                shapestate = "shapeleft.draw(win)"
            enemy = randrange(0,4)
            test = 4
            if enemy == 1:
                    if e1drawstate == 0:
                            enemy1.draw(win)
                            e1drawstate = 1
                    elif e1drawstate == 1:
                            enemy1state = (enemy1state) - 4
                            while enemy1state != 15:
                                    test = (test) + 1
                                    enemy1state = enemy1state + 4
                                    while test == 5:
                                            test = (test) - 1
                                            for i in range(5):
                                                    enemy1.move(10,0)
                                                    test = (test) + 1
                                                    buffer = (buffer) + 1
                                                    print(buffer)
                                                    if key == "Left" and buffer == 40:
                                                        enemy1.undraw()
                                                        buffer = 0
                                                    elif key != "Left" and buffer == 40:
                                                        shapedown.undraw()
                                                        shapeleft.undraw()
                                                        shaperight.undraw()
                                                        shapeup.undraw()

                                                        tfour.draw(win)
                                                        
                                                        win.getMouse()
                                                        win.close()
                                                        
    						

			#elif enemy == 4:
		#	enemy2 = Circle(Point(500, 0), 25)
		#	enemy2.setFill("white")
		#	enemy2.setOutline("dark gray")
		#	enemy2.setWidth(5)
		#	enemy2.draw(win)
        win.getMouse()
        win.close()
