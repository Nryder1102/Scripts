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
    pts = "0"
    
    t = Text(Point(0,75), "Press 'Enter' to start!")
    ttwo = Text(Point(0,55), "Use 'Up' 'Down' 'Left' 'Right' to control!")
    tthree = Text(Point(0, 35), "Use 'ESC' to quit!")
    tfour = Text(Point(0,55), "Game Over!!")
    score = Text(Point(-400,450),"test")
    score.setTextColor("white")
    score.setStyle("bold")
    score.setText("SCORE: " + pts)
    t.setTextColor("white")
    ttwo.setTextColor("white")
    tthree.setTextColor("white")
    tfour.setTextColor("red")
    t.draw(win)
    ttwo.draw(win)
    tthree.draw(win)
    score.draw(win)
    turns = 0
    enemy1 = Circle(Point(-500, 0), 25)
    enemy1.setFill("dark gray")
    enemy1.setOutline("white")
    enemy1.setWidth(5)
    enemy1state = 15
    e1drawstate = 0
    e1movestate = 0
    enemy2 = Circle(Point(500, 0), 25)
    enemy2.setFill("white")
    enemy2.setOutline("dark gray")
    enemy2.setWidth(5)
    enemy2state = 15
    e2drawstate = 0
    e2movestate = 0
    buffer = 0
    buffer2 = 0
    key = win.getKey()


    #Block to start game
    if key == "Return":
        t.undraw()
        ttwo.undraw()
        tthree.undraw()

    #Block to end game if Escape is pressed
        while key != "Escape":
            key = win.getKey()
            enemy = randrange(0,8)
    #Player Controls and Shape Movement
            if key == "Up":
                shapeup.undraw()
                shapeleft.undraw()
                shaperight.undraw()
                shapedown.undraw()
                shapeup.setOutline("sky blue")
                shapeup.setFill("light blue")
                shapeup.draw(win)
                shaperot = shapeup
                shapestate = "shapeup.draw(win)"
                e1movestate = 1
                e2movestate = 1
               # enemy1spawncheck(enemy)
               # e1move(e1drawstate)
            elif key == "Right":
                shaperight.undraw()
                shapeleft.undraw()
                shapedown.undraw()
                shapeup.undraw()
                shaperight.setOutline("red")
                shaperight.setFill("dark red")
                shaperight.draw(win)
                shaperot = shaperight
                shapestate = "shaperight.draw(win)"
                e1movestate = 1
                e2movestate = 1
              #  enemy1spawncheck(enemy)
              #  e1move(e1drawstate)
            elif key == "Down":
                shapedown.undraw()
                shapeleft.undraw()
                shaperight.undraw()
                shapeup.undraw()
                shapedown.setOutline("light blue")
                shapedown.setFill("sky blue")
                shapedown.draw(win)
                shaperot = shapedown
                shapestate = "shapedown.draw(win)"
                e1movestate = 1
                e2movestate = 1
               # enemy1spawncheck(enemy)
             #   e1move(e1drawstate)
            elif key == "Left":
                shapeleft.undraw()
                shaperight.undraw()
                shapedown.undraw()
                shapeup.undraw()
                shapeleft.setOutline("dark red")
                shapeleft.setFill("red")
                shapeleft.draw(win)
                shaperot = shapeleft
                shapestate = "shapeleft.draw(win)"
                e1movestate = 1
                e2movestate = 1

           
               # enemy1spawncheck(enemy)
            #    e1move(e1drawstate)
    #Block to randomize enemy spawning, currently effects movement as well,
    #Trying to make movement happen every time a key is pressed instead

            if enemy == 1 and e1drawstate == 0:
                enemy1.draw(win)
                e1drawstate = 1

            if e1drawstate == 1:
                if e1movestate == 1:
                    for i in range(5):
                        enemy1.move(10,0)
                        buffer = (buffer) + 1
                        print(buffer)
                        e1movestate = 0
                    if buffer == 35:
             
                        shaperot.undraw()
                        shaperot.setOutline("#4d4d4d")
                        shaperot.setFill("black")
                        shaperot.draw(win)

            if enemy == 2 and e2drawstate == 0:
                enemy2.draw(win)
                e2drawstate = 1

            if e2drawstate == 1:
                if e2movestate == 1:
                    for i in range(10):
                        enemy2.move(-10,0)
                        buffer2 = (buffer2) + 1
                        print(buffer2)
                        e2movestate = 0
                    if buffer2 == 30:
                     
                        shaperot.undraw()
                        shaperot.setOutline("#4d4d4d")
                        shaperot.setFill("black")
                        shaperot.draw(win)
                        
            
    #Block to kill enemy
            if key == "Left" and buffer == 40:
                enemy1.undraw()
                buffer = 0
                e1drawstate = 0
                enemy1.move(100,0)
                enemy1.move(-500,0)
                pts = int(pts) + 1
                score.undraw()
                score.setText("SCORE: " + str(pts))
                score.draw(win)
           

            elif buffer == 35 and buffer2 == 30:
                enemy2.move(100,0)
                buffer2 = (buffer2) - 10
                
            elif key != "Left" and buffer == 40:
                shapedown.undraw()
                shapeleft.undraw()
                shaperight.undraw()
                shapeup.undraw()
                enemy1.move(100,0)
                tfour.draw(win)
                win.getMouse()
                win.close()

            
               


            if key == "Right" and buffer2 == 40:
                enemy2.undraw()
                buffer2 = 0
                e2drawstate = 0
                enemy2.move(-100,0)
                enemy2.move(500,0)
                pts = int(pts) + 1
                score.undraw()
                score.setText("SCORE: " + str(pts))
                score.draw(win)
              

            elif key != "Right" and buffer2 == 40:
                shapedown.undraw()
                shapeleft.undraw()
                shaperight.undraw()
                shapeup.undraw()
                enemy2.move(-100,0)
                tfour.draw(win)                    
                win.getMouse()
                win.close()
                                                                
           
            if buffer == 0 or buffer2 == 0:
                win.setBackground("black")
            if buffer == 35 or buffer2 == 30:
                win.setBackground("#a30202")
                



        win.getMouse()
        win.close()
