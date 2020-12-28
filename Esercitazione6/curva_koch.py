import g2d_pyg as g2d
import math

def move_pen(start: (float, float), length: float, angle: float) -> (float, float):
    x, y = start
    x1 = x + math.cos(angle) * length
    y1 = y + math.sin(angle) * length
    g2d.draw_line((int(x), int(y)), (int(x1), int(y1)))
    return (x1, y1)

def koch_curve(start: (float, float), length: float, angle: float):
    if length <5:
        move_pen(start,length, angle)
    else:
        lun3=length/3

        pos = move_pen(start, lun3, angle)
        koch_curve(start, lun3, angle)

        angle=angle-math.pi/3
        koch_curve(pos, lun3, angle)
        pos = move_pen(pos, lun3, angle)
        
        angle=angle-(-2*math.pi/3)
        koch_curve(pos, lun3, angle)
        pos = move_pen(pos, lun3, angle)

        angle=angle-(math.pi/3)
        koch_curve(pos, lun3, angle)
        pos = move_pen(pos, lun3, angle)
        
        return pos


def main():
    g2d.init_canvas((700, 700))
    g2d.set_color((255,0,0))

    koch_curve((0,600), 700, 0)

    g2d.main_loop()

main()


