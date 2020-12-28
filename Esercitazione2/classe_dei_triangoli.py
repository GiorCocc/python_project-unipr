from math import sqrt

class Triangle:
    def __init__(self, x:float, y:float, z:float):
        self._x=x
        self._y=y
        self._z=z
    
    def heron(self) -> float:
        s=(self._x+self._y+self._z)/2
        area = sqrt(s * (s-self._x) * (s-self._y) * (s-self._z))
        return area
    
    def perimeter(self) -> float:
        p=self._x+self._y+self._z
        return p

        

def main():
    lato1=float(input("Dammi la misura del primo lato: "))
    lato2=float(input("Dammi la misura del secondo lato: "))
    lato3=float(input("Dammi la misura del terzo lato: "))

    triangolo=Triangle(lato1,lato2,lato3)
    print("Il perimetro del triangolo è: ", triangolo.perimeter())
    print("L'area del triangolo è: ", triangolo.heron())

main()