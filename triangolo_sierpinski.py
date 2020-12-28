import g2d_pyg as g2d

def triangle(x,y,w,h, level):
    # caso base
    if level ==0 or w<5 or h<5:
        return

    w2=w/2
    h2=h/2

    # coloro solo il secondo quadrante
    g2d.fill_rect((x+w2,y,w2,h2))

    # applicazione della ricorsione su ogni quandrante rimanente
    triangle(x,y,w2,h2, level-1)
    triangle(x,y+h2,w2,h2, level-1)
    triangle(x+w2,y+h2,w2,h2, level-1)

w,h=512,512                 #uso una potenza di 2 per non avere degli errori grafici
level=5
g2d.init_canvas((w,h))

g2d.set_color((0,0,0))
g2d.fill_rect((0,0,w,h))

g2d.set_color((255,255,255))
triangle(0,0,w,h,level)

g2d.main_loop()