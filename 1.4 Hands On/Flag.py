from graphics import *
def main():
    win = GraphWin("Flag", 1000, 1000)
    win.setCoords(-90.0, -90.0, 90.0, 90.0)
    bar1 = Rectangle(Point(-90.0, -90.0), Point(-30.0, 90.0))
    bar1.setFill("green")
    bar1.draw(win)
    bar2 = Rectangle(Point(-30.0, -90.0), Point(30.0, 90.0))
    bar2.setFill("white")
    bar2.draw(win)
    bar3 = Rectangle(Point(30.0, -90.0), Point(90.0, 90.0))
    bar3.setFill("red")
    bar3.draw(win)



main()
