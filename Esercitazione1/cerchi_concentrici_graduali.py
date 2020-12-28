import g2d

g2d.init_canvas((600,600))

count=0
i=int(input("Quanti cerchi vuoi disegnare?"))
r=255/i

while count<i:
    g2d.set_color((255-count*r,0,0))
    g2d.fill_circle((300,300),200-count*10)
    count=count+1

g2d.main_loop()
