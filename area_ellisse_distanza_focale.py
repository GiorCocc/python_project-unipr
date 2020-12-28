import math

class Elipse:
    def __init__(self, a:float, b:float):
        self._a=a
        self._b=b

    def area(self) ->float:
         res=math.pi*self._a*self._b
         return res

    def focal_distance(self) ->float:
        res=2*math.sqrt(abs(self._a**2 - self._b**2))
        return res

def main():
    first=float(input("valore del semiasse a "))
    second=float(input("valore del semiasse b "))
    e=Elipse(first,second)
    area=e.area()
    focal=e.focal_distance()
    print("L'area è ", area, "e la distanza focale è", focal)

main()