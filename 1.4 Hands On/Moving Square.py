def main():
	win = GraphWin("Test", 1000, 1000)
	shape = Rectangle(Point(50,50), Point(100,100))
	shape.setOutline("red")
	shape.setFill("red")
	shape.draw(win)
	for i in range(10):
		p = win.getMouse()
		c = shape.getCenter()
		dx = p.getX() - c.getX()
		dy = p.getY() - c.getY()
		shape.move(dx,dy)
	win.close()