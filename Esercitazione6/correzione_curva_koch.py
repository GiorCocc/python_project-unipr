import math
import g2d_pyg as g2d

def move_pen(start: (float, float), length: float, angle: float) -> (float, float):
    x, y = start
    x1 = x + math.cos(angle) * length
    y1 = y + math.sin(angle) * length
    g2d.draw_line((int(x), int(y)), (int(x1), int(y1)))
    return (x1, y1)

    

def main():
    g2d.init_canvas((600, 600))
    g2d.set_color((255,0,0))

    koch_curve((0,300), 600, 0)

    g2d.main_loop()

main()