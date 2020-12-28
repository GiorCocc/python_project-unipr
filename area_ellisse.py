import math

def ellipse_area(a: float, b: float) -> float:
    return math.pi*a*b

def main():
    first=float(input("valore del semiasse a"))
    second=float(input("valore del semiasse b"))
    area= ellipse_area(first, second)
    print(area)

main()
