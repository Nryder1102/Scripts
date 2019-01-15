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
    shapecenter = Circle(Point(0,0), 13)
    shapecenter.setFill("black")
    shapecenter.setOutline("silver")
    shapecenter.setWidth(3)
    pts = "0"
    arm = "0"
    t = Text(Point(0,75), "Press 'Enter' to start!")
    ttwo = Text(Point(0,55), "Use 'Up' 'Down' 'Left' 'Right' to control!")
    tthree = Text(Point(0, 35), "Use 'ESC' to quit!")
    tfour = Text(Point(0,55), "Game Over!!")
    score = Text(Point(-400,450),"test")
    armor = Text(Point(-300,450), "test")
    score.setTextColor("white")
    score.setStyle("bold")
    score.setText("SCORE: " + pts)
    armor.setTextColor("white")
    armor.setStyle("bold")
    armor.setText("ARMOR: " + arm)
    t.setTextColor("white")
    ttwo.setTextColor("white")
    tthree.setTextColor("white")
    tfour.setTextColor("black")
    tfour.setStyle("bold")
    t.draw(win)
    ttwo.draw(win)
    tthree.draw(win)
    score.draw(win)
    armor.draw(win)
    turns = 0
    enemy1 = Circle(Point(-500, 0), 25)
    enemy1.setFill("dark gray")
    enemy1.setOutline("white")
    enemy1.setWidth(5)
    enemy1state = 15
    e1drawstate = 0
    e1movestate = 0
    enemy2 = Circle(Point(500, 0), 25)
    enemy2.setFill("black")
    enemy2.setOutline("dark gray")
    enemy2.setWidth(5)
    enemy2state = 15
    e2drawstate = 0
    e2movestate = 0
    enemy3 = Rectangle(Point(-20,500), Point(20,460))
    enemy3.setFill("black")
    enemy3.setWidth(0)
    enemy3state = 15
    e3drawstate = 0
    e3movestate = 0
    enemy4 = Rectangle(Point(-15,-500), Point(15,-470))
    enemy4.setFill("black")
    enemy4.setWidth(0)
    enemy4state = 15
    e4drawstate = 0
    e4movestate = 0
    power5 = Rectangle(Point(-10,500), Point(10,480))
    power5.setFill("silver")
    power5.setOutline("purple")
    power5state = 15
    p5drawstate = 0
    p5movestate = 0
    buffer = 0
    buffer2 = 0
    buffer3 = 0
    buffer4 = 0
    buffer5 = 0
    armorstate = 0
    key2 = win.getKey()


    #Block to start game
    if key2 != "Escape":
        t.undraw()
        ttwo.undraw()
        tthree.undraw()
        key2 = 0
        key = 0
    #Block to end game if Escape is pressed
        while key != "Escape":
            key = win.getKey()
            enemy = randrange(0,16)
    #Player Controls and Shape Movement
            if key == "Up":
                shapeup.undraw()
                shapeleft.undraw()
                shaperight.undraw()
                shapedown.undraw()
                shapecenter.undraw()
                if armorstate == 0:
                    shapecenter.setOutline("black")
                    shapecenter.setFill("sky blue")
                    shapeup.setOutline("sky blue")
                    shapeup.setFill("light blue")
                    shapeup.setWidth(0)
                elif armorstate != 0:
                    shapecenter.setFill("lime green")
                    shapecenter.setOutline("silver")
                    shapeup.setFill("purple")
                    shapeup.setOutline("silver")
                    shapeup.setWidth(5)
                shapeup.draw(win)
                shaperot = shapeup
                shapestate = "shapeup.draw(win)"
                shapecenter.draw(win)
                e1movestate = 1
                e2movestate = 1
                e3movestate = 1
                e4movestate = 1
                p5movestate = 1
               # enemy1spawncheck(enemy)
               # e1move(e1drawstate)
            elif key == "Right":
                shaperight.undraw()
                shapeleft.undraw()
                shapedown.undraw()
                shapeup.undraw()
                shapecenter.undraw()
                if armorstate == 0:
                    shapecenter.setOutline("black")
                    shapecenter.setFill("red")
                    shaperight.setOutline("red")
                    shaperight.setFill("dark red")
                    shaperight.setWidth(0)
                elif armorstate != 0:
                    shapecenter.setFill("lime green")
                    shapecenter.setOutline("silver")
                    shaperight.setFill("purple")
                    shaperight.setOutline("silver")
                    shaperight.setWidth(5)
                shaperight.draw(win)
                shaperot = shaperight
                shapestate = "shaperight.draw(win)"
                shapecenter.draw(win)
                e1movestate = 1
                e2movestate = 1
                e3movestate = 1
                e4movestate = 1
                p5movestate = 1
              #  enemy1spawncheck(enemy)
              #  e1move(e1drawstate)
            elif key == "Down":
                shapedown.undraw()
                shapeleft.undraw()
                shaperight.undraw()
                shapeup.undraw()
                shapecenter.undraw()
                if armorstate == 0:
                    shapecenter.setOutline("black")
                    shapecenter.setFill("light blue")
                    shapedown.setOutline("light blue")
                    shapedown.setFill("sky blue")
                    shapedown.setWidth(0)
                elif armorstate != 0:
                    shapecenter.setFill("lime green")
                    shapecenter.setOutline("silver")
                    shapedown.setFill("purple")
                    shapedown.setOutline("silver")
                    shapedown.setWidth(5)
                shapedown.draw(win)
                shaperot = shapedown
                shapestate = "shapedown.draw(win)"
                shapecenter.draw(win)
                e1movestate = 1
                e2movestate = 1
                e3movestate = 1
                e4movestate = 1
                p5movestate = 1
               # enemy1spawncheck(enemy)
             #   e1move(e1drawstate)
            elif key == "Left":
                shapeleft.undraw()
                shaperight.undraw()
                shapedown.undraw()
                shapeup.undraw()
                shapecenter.undraw()
                if armorstate == 0:
                    shapecenter.setOutline("black")
                    shapecenter.setFill("dark red")
                    shapeleft.setOutline("dark red")
                    shapeleft.setFill("red")
                    shapeleft.setWidth(0)
                elif armorstate != 0:
                    shapecenter.setFill("lime green")
                    shapecenter.setOutline("silver")
                    shapeleft.setFill("purple")
                    shapeleft.setOutline("silver")
                    shapeleft.setWidth(5)
                shapeleft.draw(win)
                shaperot = shapeleft
                shapestate = "shapeleft.draw(win)"
                shapecenter.draw(win)
                e1movestate = 1
                e2movestate = 1
                e3movestate = 1
                e4movestate = 1
                p5movestate = 1
           
               # enemy1spawncheck(enemy)
            #    e1move(e1drawstate)
    #Block to randomize enemy spawning, currently effects movement as well,
    #Trying to make movement happen every time a key is pressed instead



            #Enemy 1 Spawn + Move
            if enemy == 1 and e1drawstate == 0:
                enemy1.setFill("dark gray")
                enemy1.setOutline("white")
                enemy1.draw(win)
                e1drawstate = 1

            if e1drawstate == 1:
                if e1movestate == 1:
                    for i in range(5):
                        enemy1.move(10,0)
                        buffer = (buffer) + 1
                       # print(buffer)
                        e1movestate = 0
                    if buffer == 35:
                        enemy1.undraw()
                        enemy1.setFill("dark gray")
                        enemy1.setOutline("black")            
                        shaperot.undraw()
                        shapecenter.undraw()
                        shapecenter.setFill("#a30202")
                        shapecenter.setOutline("#4d4d4d")
                        shaperot.setOutline("#4d4d4d")
                        shaperot.setFill("black")
                        shaperot.draw(win)
                        shapecenter.draw(win)

                    if buffer == 35 and e1drawstate == 1:
                        enemy1.undraw()
                        enemy1.setFill("#4d4d4d")
                        enemy1.setOutline("#1c1c1c")
                        enemy1.draw(win)

                  
            #Enemy 2 Spawn + Move
            if enemy == 2 and e2drawstate == 0:
                enemy2.setFill("white")
                enemy2.setOutline("dark gray")
                enemy2.draw(win)
                e2drawstate = 1

            if e2drawstate == 1:
                if e2movestate == 1:
                    for i in range(10):
                        enemy2.move(-10,0)
                        buffer2 = (buffer2) + 1
                       # print(buffer2)
                        e2movestate = 0
                    if buffer2 == 30:
                        shaperot.undraw()
                        shapecenter.undraw()
                        shapecenter.setFill("#a30202")
                        shapecenter.setOutline("#4d4d4d")
                        shaperot.setOutline("#4d4d4d")
                        shaperot.setFill("black")
                        shaperot.draw(win)
                        shapecenter.draw(win)

                    if buffer2 == 30 and e2drawstate == 1:
                        enemy2.undraw()
                        enemy2.setFill("#4d4d4d")
                        enemy2.setOutline("#1c1c1c")
                        enemy2.draw(win)



            #Enemy 3 Spawn + Move
            if enemy == 3 and e3drawstate == 0:
                    enemy3.setFill("black")
                    enemy3.setOutline("black")
                    enemy3.draw(win)
                    e3drawstate = 1

            if e3drawstate == 1:
                if e3movestate == 1:
                    for i in range(1):
                        enemy3.move(0,-25)
                        buffer3 = (buffer3) + 1
                        print(buffer3)
                        e3movestate = 0

                if buffer3 == 14:
                        shaperot.undraw()
                        shapecenter.undraw()
                        shapecenter.setFill("#a30202")
                        shapecenter.setOutline("#4d4d4d")
                        shaperot.setOutline("#4d4d4d")
                        shaperot.setFill("black")
                        shaperot.draw(win)                 
                        shapecenter.draw(win)
                


            #Enemy 4 Spawn + Move
            if enemy == 4 and e4drawstate == 0:
                    enemy4.setFill("black")
                    enemy4.setOutline("black")
                    enemy4.draw(win)
                    e4drawstate = 1

            if e4drawstate == 1:
                if e4movestate == 1:
                    for i in range(1):
                        enemy4.move(0,50)
                        buffer4 = (buffer4) + 1
                        print(buffer4)
                        e4movestate = 0

                if buffer4 == 7:
                        shaperot.undraw()
                        shapecenter.undraw()
                        shapecenter.setFill("#a30202")
                        shapecenter.setOutline("#4d4d4d")
                        shaperot.setOutline("#4d4d4d")
                        shaperot.setFill("black")
                        shaperot.draw(win)
                        shapecenter.draw(win)

               

            #Power 1(5) Spawn + Move
            if enemy == 5 and p5drawstate == 0:
                    power5.draw(win)
                    p5drawstate = 1

            if p5drawstate == 1:

                if p5movestate == 1:
                    for i in range(1):
                        power5.move(0,-10)
                        buffer5 = (buffer5) + 1
                       # print(buffer3)
                        p5movestate = 0

                if buffer5 == 40:
                        shaperot.undraw()
                        shapecenter.undraw()
                        shapecenter.setFill("green")
                        shapecenter.setOutline("silver")
                        shaperot.setOutline("silver")
                        shaperot.setFill("purple")
                        shaperot.setWidth(5)
                        shaperot.draw(win)
                        shapecenter.draw(win)
                        armorstate = (armorstate) + 1
                        arm = int(arm) + 1
                        armor.undraw()
                        armor.setText("ARMOR: " + str(arm))
                        armor.draw(win)
                        power5.undraw()
                        power5.move(0,-100)
                        power5.move(0,500)
                        buffer5 = 0
                        p5drawstate = 0


                        
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
            elif buffer == 35 and buffer3 == 14:
                enemy3.move(0,25)
                buffer3 = (buffer3) - 1
            elif buffer2 == 30 and buffer3 == 14:
                enemy3.move(0,25)
                buffer3 = (buffer3) - 1
            elif buffer4 == 7 and buffer3 == 14:
                enemy3.move(0,25)
                buffer3 = (buffer3) - 1
            
                
            elif key != "Left" and buffer == 40 and armorstate == 0:
                shapedown.undraw()
                shapeleft.undraw()
                shaperight.undraw()
                shapeup.undraw()
                shapecenter.undraw()
                enemy1.move(100,0)
                tfour.draw(win)
                win.getMouse()
                win.close()

            elif armorstate != 0 and buffer == 40:
                enemy1.undraw()
                buffer = 0
                e1drawstate = 0
                enemy1.move(100,0)
                enemy1.move(-500,0)
                armorstate = (armorstate) - 1
                arm = int(arm) - 1
                armor.undraw()
                armor.setText("ARMOR: " + str(arm))
                armor.draw(win)

            
               


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
              

            elif key != "Right" and buffer2 == 40 and armorstate == 0:
                shapedown.undraw()
                shapeleft.undraw()
                shaperight.undraw()
                shapeup.undraw()
                shapecenter.undraw()
                enemy2.move(-100,0)
                tfour.draw(win)                    
                win.getMouse()
                win.close()
                                                                

            elif armorstate != 0 and buffer2 == 40:
                enemy2.undraw()
                buffer2 = 0
                e2drawstate = 0
                enemy2.move(-100,0)
                enemy2.move(500,0)
                armorstate = (armorstate) - 1
                arm = int(arm) - 1
                armor.undraw()
                armor.setText("ARMOR: " + str(arm))
                armor.draw(win)




            if key == "Up" and buffer3 == 15:
                enemy3.undraw()
                buffer3 = 0
                e3drawstate = 0
                enemy3.move(0,-100)
                enemy3.move(0,475)
                pts = int(pts) + 1
                score.undraw()
                score.setText("SCORE: " + str(pts))
                score.draw(win)
                        
            elif key != "Up" and buffer3 == 15 and armorstate == 0:
                shapedown.undraw()
                shapeleft.undraw()
                shaperight.undraw()
                shapeup.undraw()
                shapecenter.undraw()
                enemy3.move(0,-100)
                tfour.draw(win)
                win.getMouse()
                win.close()

            elif armorstate != 0 and buffer3 == 15:
                enemy3.undraw()
                buffer3 = 0
                e3drawstate = 0
                enemy3.move(0,-100)
                enemy3.move(0,500)
                armorstate = (armorstate) - 1
                arm = int(arm) - 1
                armor.undraw()
                armor.setText("ARMOR: " + str(arm))
                armor.draw(win)





            if key == "Down" and buffer4 == 8:
                enemy4.undraw()
                buffer4 = 0
                e4drawstate = 0
                enemy4.move(0,100)
                enemy4.move(0,-500)
                pts = int(pts) + 1
                score.undraw()
                score.setText("SCORE: " + str(pts))
                score.draw(win)
                        
            elif key != "Down" and buffer4 == 8 and armorstate == 0:
                shapedown.undraw()
                shapeleft.undraw()
                shaperight.undraw()
                shapeup.undraw()
                shapecenter.undraw()
                enemy4.move(0,100)
                tfour.draw(win)
                win.getMouse()
                win.close()

            elif armorstate != 0 and buffer4 == 8:
                enemy4.undraw()
                buffer4 = 0
                e4drawstate = 0
                enemy4.move(0,100)
                enemy4.move(0,-500)
                armorstate = (armorstate) - 1
                arm = int(arm) - 1
                armor.undraw()
                armor.setText("ARMOR: " + str(arm))
                armor.draw(win)
           




           


            



            if buffer == 0 or buffer2 == 0 or buffer3 == 0 or buffer4 == 0:
                win.setBackground("black")
                if e3drawstate == 1:
                    enemy3.undraw()
                    enemy3.setOutline("black")
                    enemy3.setFill("black")
                    enemy3.draw(win)
                if e4drawstate == 1:
                    enemy4.undraw()
                    enemy4.setFill("black")
                    enemy4.setOutline("black")
                    enemy4.draw(win)
            if buffer == 35 or buffer2 == 30 or buffer3 == 14 or buffer4 == 7:
                win.setBackground("#a30202")
                if e3drawstate == 1:
                    enemy3.undraw()
                    enemy3.setFill("#6d0000")
                    enemy3.setOutline("#6d0000")
                    enemy3.draw(win)
                if e4drawstate == 1:
                    enemy4.undraw()
                    enemy4.setFill("#6d0000")
                    enemy4.setOutline("#6d0000")
                    enemy4.draw(win)
            if pts == 75:
                e1drawstate = 3
                e2drawstate = 3
                e3drawstate = 3
                e4drawstate = 3
                p5drawstate = 3
                

        
        
        win.getMouse()
        win.close()
