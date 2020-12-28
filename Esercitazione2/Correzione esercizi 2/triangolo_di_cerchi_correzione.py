import g2d

size=600
g2d.init_canvas(size,size)

n=int(g2d.prompt("n? "))
d=60//n
r=d//2

for y in range(1,n+1):
    for x in range(1,y+1):
        xc=x*d-r
        yc=y*d-r
        g2d.fill_circle((xc, yc), r)
    print("")

g2d.main_loop()