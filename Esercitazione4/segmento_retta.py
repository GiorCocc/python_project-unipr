def slope(punto_1, punto_2) -> float:
    x1,y1=punto_1
    x2,y2=punto_2
    m = (y2-y1) / (x2-x1)
    return m

def intercept(punto_1, punto_2) -> float:
    x1,y1=punto_1
    x2,y2=punto_2
    m = (y2-y1) / (x2-x1)
    b=y1-m*x1
    return b

def main():
    x1=float(input("Dammi la x del punto 1"))
    y1=float(input("Dammi la y del punto 1"))
    x2=float(input("Dammi la x del punto 2"))
    y2=float(input("Dammi la y del punto 2"))
    punto_1=x1,y1
    punto_2=x2,y2
    print("Il coefficiente angolare della retta è:", slope(punto_1, punto_2))
    print("La quota all'origine della retta è:", intercept(punto_1, punto_2))

main()