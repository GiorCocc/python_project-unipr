from random import randint

class TargetShooting:
    def __init__(self):
        self._centers=[]
        self._n=randint(1,11)

        for i in range (self._n):
            x=randint(0,599)
            y=randint(0,599)
            center=(x,y)
            self._centers.append(center)
        print(self._centers)


    def shoot(self, xs:int, ys:int) -> bool:
        hit=False
        for center in self._centers:
            xc,yc =center
            #controllare la distanza euclidea tra i due centri
            if (xc-25<=xs<=xc+25)and(yc-25<=ys<=yc+25):
                hit=True
        return hit

def main():
    s=str(input("Vuoi sparare [si/no]?"))
    while s=="si":
        t=TargetShooting()
        x=int(input("Dimmi dove vuoi sparare (da 0 a 600) x="))
        y=int(input("Dimmi dove vuoi sparare (da 0 a 600) y="))
        
        if (t.shoot(x,y)):
            s=str(print("Hai centrato il bersaglio! Vuoi riprovare [si/no]?")) 
            t=TargetShooting()
        else:
            s=str(input("Non hai centrato il bersaglio! Vuoi riprovare [si/no]?"))

main()