class Segmento:
    def __init__(self, punto_1, punto_2):
        self._x1, self._y1=punto_1
        self._x2, self._y2=punto_2
        

    def slope(self) -> float:
        m = (self._y2-self._y1) / (self._x2-self._x1)
        return m

    def intercept(self) -> float:
        m = (self._y2-self._y1) / (self._x2-self._x1)
        b=self._y1-m*self._x1
        return b

def main():
    x1=float(input("Dammi la x del punto 1"))
    y1=float(input("Dammi la y del punto 1"))
    x2=float(input("Dammi la x del punto 2"))
    y2=float(input("Dammi la y del punto 2"))
    punto_1=x1,y1
    punto_2=x2,y2
    s=Segmento(punto_1,punto_2)
    print("Il coefficiente angolare della retta è:", s.slope())
    print("La quota all'origine della retta è:", s.intercept())
main()