from graphics import *
def main():
    win = GraphWin("Winter", 300,300)
    win.setBackground("#b2cff0")
    win.setCoords(-100, -100, 100, 100)
    head = Circle(Point(30,20), 20)
    head.setOutline("white")
    head.setFill("white")
    head.draw(win)
    body = Circle(Point(30,-15), 25)
    body.setFill("white")
    body.setOutline("white")
    body.draw(win)
    body2 = Circle(Point(30,-60), 35)
    body2.setFill("White")
    body2.setOutline("White")
    body2.draw(win)
    eye1 = Circle(Point(21, 25), 2)
    eye1.setFill("black")
    eye1.draw(win)
    eye2 = Circle(Point(40, 25), 2)
    eye2.setFill("black")
    eye2.draw(win)

    mouth1 = Circle(Point(21, 15), 1)
    mouth1.setFill("black")
    mouth1.draw(win)
    mouth2 = Circle(Point(40, 15), 1)
    mouth2.setFill("black")
    mouth2.draw(win)
    mouth3 = Circle(Point(25, 10), 1)
    mouth3.setFill("black")
    mouth3.draw(win)
    mouth4 = Circle(Point(35, 10), 1)
    mouth4.setFill("black")
    mouth4.draw(win)
    mouth5 = Circle(Point(30, 8), 1)
    mouth5.setFill("black")
    mouth5.draw(win)

    button1 = Circle(Point(30,-15), 1.9)
    button1.setFill("black")
    button1.draw(win)
    button2 = Circle(Point(30,-25), 1.9)
    button2.setFill("black")
    button2.draw(win)
    button3 = Circle(Point(30,-5), 1.9)
    button3.setFill("black")
    button3.draw(win)
    
    
    stump = Rectangle(Point(-80, -80), Point(-60, -20))
    stump.setFill('#946e51')
    stump.setOutline("#946e51")
    stump.draw(win)
    tree = Polygon(Point(-120, -35), Point(-70, 100), Point(-20, -35))
    tree.setFill("#5c9c40")
    tree.setOutline("#5c9c40")
    tree.draw(win)
    tree2 = Polygon(Point(-120, 0), Point(-70, 100), Point(-20, 0))
    tree2.setFill("#609660")
    tree2.setOutline("#609660")
    tree2.draw(win)
    ground = Oval(Point(-130, -120), Point(130, -70))
    ground.setFill("#ebebeb")
    ground.setOutline("#ebebeb")
    ground.draw(win)
main()
