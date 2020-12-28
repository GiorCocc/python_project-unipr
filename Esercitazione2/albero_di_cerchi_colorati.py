import g2d
from random import randint

AREA_X=AREA_Y=600
g2d.init_canvas((AREA_X,AREA_Y))

n=int(input("Quante file vuoi? "))
raggio=AREA_X/((n*2))


for i in range(0,n):
    for z in range (0,i):
        r=randint(0,256)
        g=randint(0,256)
        b=randint(0,256)

        xc=(((n-i)*raggio)+(z*2*raggio))+raggio
        yc=(raggio+(raggio*i*2))-(raggio*2)

        g2d.set_color((r,g,b))
        g2d.fill_circle((xc, yc), raggio)

g2d.set_color((randint(0,256),randint(0,256),randint(0,256)))
g2d.fill_circle((AREA_X/2, AREA_Y-raggio), raggio)

g2d.main_loop()