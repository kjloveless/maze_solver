from graphics import Window
from cell import Cell

def main():
  win = Window(800, 600)
  c1 = Cell(win)
  c2 = Cell(win)
  
  c1.draw(50, 50, 200, 100)
  c2.has_bottom_wall = False
  c2.draw(100, 200, 200, 400)

  win.wait_for_close()

main()
