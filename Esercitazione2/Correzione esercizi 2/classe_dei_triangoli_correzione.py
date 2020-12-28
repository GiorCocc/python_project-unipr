class Triangle:
    def __init__(self, s1:float, s2:float, s3:float):
        self._a=s1
        self._b=s2
        self._c=s3

    def perimeter(self)-> float:
        result=self._a+self._b+self._c
        return result

def heron(a: float, b: float, c:float) ->float:
    s=(a+b+c)/2
    area = (s * (s-a) * (s-b) * (s-c))**0.5
    return area

def main():
    s1=float(input("s1?"))
    s2=float(input("s2?"))
    s3=float(input("s3?"))
    t=Triangle(s1,s2,s3)
    print("Perimetro=", t.perimeter())


main()