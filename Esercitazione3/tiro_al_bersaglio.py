from random import randint

class TargetShooting:
    def __init__(self):
        self._x = randint(0,575)
        self._y = randint(0,575)
        self._r = 25


    def shoot(self, x,y):
        if (x==self._x or x==(self._x+self._r) or x==(self._x-self._r))  and (y==self._y or y==(self._y+self._r) or y==(self._y-self._r)):
            return True
        else: False


def main():
    t=TargetShooting()
    n=randint(1,15)
    target=[TargetShooting()]*n
    ris=False

    s=str(input("Vuoi sparare [si/no]?"))
    while s=="si":
        x=int(input("Dimmi dove vuoi sparare (da 0 a 600) x="))
        y=int(input("Dimmi dove vuoi sparare (da 0 a 600) y="))

        for t in target:
            if(t.shoot(x,y)):
                ris=True
                print("Hai centrato il bersaglio!")
        if ris==False:
            s=str(input("Non hai centrato il bersaglio! Vuoi riprovare [si/no]?"))
        else:
            s=str(input("Hai vinto! Vuoi riprovare [si/no]?"))

main()


