from random import randint

w,h=5,5
xp,yp=0,0

#parametri del mostro
xm=randint(0,w-1)
ym=randint(0,h-1)


#parametri per il tesoro
xg=randint(0,w-1)
yg=randint(0,h-1)


while xm==xp and ym==yp:
    xm=randint(0,w-1)
    ym=randint(0,h-1)
    #print("il mostro è in posizione:", xm, ym)  #for debug

while (xg==xm and yg==ym) or (xg==xp and yg==yp):
    xg=randint(0,w-1)
    yg=randint(0,h-1)
    #print("il tesoro è in posizione:", xm, ym)  #for debug

while (xp!=xm or yp!=ym) and (xp!=xg or yp!=yg):
    #print(xp,yp)    #for debug
    scelta=input("Che mossa vuoi effettuare: [su,giu,dx,sx]")
    
    if scelta=="su" and yp<=h:
        yp+=1
        #print(xp,yp)    #for debug
    elif scelta=="giu" and yp>0:
        yp-=1
        #print(xp,yp)    #for debug
    elif scelta=="dx" and xp<=w:
        xp+=1
        #print(xp,yp)    #for debug
    elif scelta=="sx"and xp>0:
        xp-=1
        #print(xp,yp)    #for debug

    if xp==xg and yp==yg:
        print("Hai raggiunto l'oro!")
    if xp==xm and yp==ym:
        print("Sei stato catturato dal mostro!")
    