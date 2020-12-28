from random import randint
import g2d

g2d.init_canvas((600,600))

count=0
x=200

while x>10:
    r=randint(0,256)
    b=randint(0,256)
    g=randint(0,256)

    g2d.set_color((r,g,b))
    g2d.fill_circle((300,300),x)
    
    count=count+1
    x=200-count*randint(0,x-1)


g2d.main_loop()
