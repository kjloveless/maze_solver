from graphics import Window, Point, Line

def main():
  win = Window(800, 600)
  p1 = Point(10, 50)
  p2 = Point(75, 200)
  l = Line(p1, p2)

  win.draw_line(l, "red")

  win.wait_for_close()

main()
