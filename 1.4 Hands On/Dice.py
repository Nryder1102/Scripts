from graphics import *
def main():
    win = GraphWin("Dice", 900,900)
    win.setCoords(-450,-450,450,450)
    d1 = Rectangle(Point(400,400), Point(300,300))
    d1.draw(win)
    d1dot1 = Circle(Point(380, 380), 10)
    d1dot1.setFill("black")
    d1dot1.draw(win)
    d1dot2 = Circle(Point(380, 350), 10)
    d1dot2.setFill("black")
    d1dot2.draw(win)
    d1dot3 = Circle(Point(380, 320), 10)
    d1dot3.setFill("black")
    d1dot3.draw(win)
    d1dot4 = Circle(Point(320, 380), 10)
    d1dot4.setFill("black")
    d1dot4.draw(win)
    d1dot5 = Circle(Point(320, 350), 10)
    d1dot5.setFill("black")
    d1dot5.draw(win)
    d1dot6 = Circle(Point(320, 320), 10)
    d1dot6.setFill("black")
    d1dot6.draw(win)

    d2 = Rectangle(Point(250,400), Point(150,300))
    d2.draw(win)
    d2dot1 = Circle(Point(230, 380), 10)
    d2dot1.setFill("black")
    d2dot1.draw(win)
    d2dot2 = Circle(Point(230, 320), 10)
    d2dot2.setFill("black")
    d2dot2.draw(win)
    d2dot3 = Circle(Point(170, 320), 10)
    d2dot3.setFill("black")
    d2dot3.draw(win)
    d2dot4 = Circle(Point(170, 380), 10)
    d2dot4.setFill("black")
    d2dot4.draw(win)
    d2dot5 = Circle(Point(200, 350), 10)
    d2dot5.setFill("black")
    d2dot5.draw(win)

    d3 = Rectangle(Point(100,400), Point(0,300))
    d3.draw(win)
    d3dot1 = Circle(Point(20, 380), 10)
    d3dot1.setFill("black")
    d3dot1.draw(win)
    d3dot2 = Circle(Point(20, 320), 10)
    d3dot2.setFill("black")
    d3dot2.draw(win)
    d3dot3 = Circle(Point(80, 320), 10)
    d3dot3.setFill("black")
    d3dot3.draw(win)
    d3dot4 = Circle(Point(80, 380), 10)
    d3dot4.setFill("black")
    d3dot4.draw(win)

    d4 = Rectangle(Point(-250,400), Point(-150,300))
    d4.draw(win)
    d4dot1 = Circle(Point(20, 380), 10)
    d4dot1.setFill("black")
    d4dot1.draw(win)
    d4dot2 = Circle(Point(20, 320), 10)
    d4dot2.setFill("black")
    d4dot2.draw(win)
    d4dot3 = Circle(Point(80, 320), 10)
    d4dot3.setFill("black")
    d4dot3.draw(win)

main()
