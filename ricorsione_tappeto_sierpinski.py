import g2d_pyg as g2d

def sierpinski(x,y, w, h):
    w3,h3=w//3, h//3

    if w3<1 or h3<1:
        return
    for row in range (3):
        for col in range (3):
            x3,y3=x+col*w3, y+row*w3
            if row==1 and col==1:
                g2d.fill_rect((x+col*w3, y+row*w3, w3, h3))
            else:
                sierpinski(x3, y3, w3, h3)

def main():
    w,h=600,600

    g2d.init_canvas((w,h))
    sierpinski(0,0,w,h)
    g2d.main_loop()

main()