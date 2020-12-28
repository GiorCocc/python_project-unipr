import g2d_pyg as g2d
import math

def move_pen(start: (float, float), length: float, angle: float) -> (float, float):
    x, y = start
    x1 = x + math.cos(angle) * length
    y1 = y + math.sin(angle) * length
    g2d.draw_line((int(x), int(y)), (int(x1), int(y1)))
    return (x1, y1)

def albero(start, lunghezza, angolo):
    if lunghezza<=5:
        pos=move_pen(start,lunghezza, angolo)
    else:
        pos=move_pen(start,lunghezza, angolo)
        lunghezza=4*lunghezza/5
        # pos1=move_pen(pos, lunghezza, angolo-math.pi/6)
        albero(pos, lunghezza, angolo-math.pi/6)
        albero(pos, lunghezza, angolo+math.pi/6)

def main():
    g2d.init_canvas((600, 600))


    pos, side, angle = (300, 600), 100, -math.pi/2  # →
    albero(pos, side, angle)

    g2d.main_loop()

main()
