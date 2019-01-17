from graphics import *
def main():
    win = GraphWin("Target", 1000, 1000)
    win.setCoords(-500.0, -500.0, 500.0, 500.0)
    win.setBackground("gray")
    ring1 = Circle(Point(0,0), 500)
    ring1.setFill("white")
    ring2 = Circle(Point(0,0), 400)
    ring2.setFill("black")
    ring3 = Circle(Point(0,0), 300)
    ring3.setFill("blue")
    ring4 = Circle(Point(0,0), 200)
    ring4.setFill("red")
    ring5 = Circle(Point(0,0), 100)
    ring5.setFill("yellow")
    ring1.draw(win)
    ring2.draw(win)
    ring3.draw(win)
    ring4.draw(win)
    ring5.draw(win)


main()
