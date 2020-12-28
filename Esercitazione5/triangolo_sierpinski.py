import g2d_pyg as g2d

def sierp(x,y,w,h):
    if w<1 and h<1:
        return

    w2, h2 = w/2, h/2
    g2d.fill_rect((x+w2, y, w2, h2))

    sierp(x,y,w2,h2)
    sierp(x,y+h2,w2,h2)
    sierp(x+w2,y,w2,h2)

    

def main():
    width,height=512,512
    g2d.init_canvas((width,height))

    g2d.set_color((0,0,0))      #sfondo nero
    g2d.fill_rect((0,0,width,height))
    g2d.set_color((255,255,255))

    sierp(0,0,width,height)
    g2d.main_loop()

main()