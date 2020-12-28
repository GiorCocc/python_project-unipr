from math import sqrt

def heron(a:float, b:float, c:float) -> float:
    s=(a+b+c)/2
    area = sqrt(s * (s-a) * (s-b) * (s-c))
    return area

def main():
    lato1=float(input("Dammi la misura del primo lato: "))
    lato2=float(input("Dammi la misura del secondo lato: "))
    lato3=float(input("Dammi la misura del terzo lato: "))

    erone=heron(lato1, lato2, lato3)
    print("L'area del triangolo è: ", erone)

main()