import g2d_pyg as g2d

def h_tree(x,y,w,h, level):
    # per avere una limitazione nella stampa
    if level==0:
        return
    # caso base
    if w<10 or h<10:
        return
    
    g2d.draw_line((x+1*w/4, y+1*h/4) , (x+1*w/4, y+3*h/4))  #linea verticale
    g2d.draw_line((x+3*w/4, y+1*h/4) , (x+3*w/4, y+3*h/4))  #linea orizzontale
    g2d.draw_line((x+1*w/4, y+2*h/4) , (x+3*w/4, y+2*h/4))  #linea verticale

    # ricorsione per i 4 quadranti ottenuti dalla divisione dell'area
    h_tree(x, y, w/2, h/2, level-1)
    h_tree(x+w/2, y, w/2, h/2, level-1)
    h_tree(x+w/2, y+h/2, w/2, h/2, level-1)
    h_tree(x, y+h/2, w/2, h/2, level-1)


def main():
    g2d.init_canvas((600, 600))
    h_tree(0+10, 0+10, 600-20, 600-20, 10)
    g2d.main_loop()

main()