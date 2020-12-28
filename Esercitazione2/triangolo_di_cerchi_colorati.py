import g2d
from random import randint

g2d.init_canvas((600,600))
r=20
x=r
y=r

n=11
while n>10:
    n=int(input("Che numero desideri? "))
for i in range (1,n+1):
    for z in range (1,i):
        g2d.set_color((randint(0,256), randint(0,256), randint(0,256)))
        g2d.fill_circle((x*z*2,y*i*2), r)
g2d.main_loop()