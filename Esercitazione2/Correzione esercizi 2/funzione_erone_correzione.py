def heron(a: float, b: float, c:float) ->float:
    s=(a+b+c)/2
    area = (s * (s-a) * (s-b) * (s-c))**0.5
    return area

def main():
    s1=float(input("s1?"))
    s2=float(input("s2?"))
    s3=float(input("s3?"))
    print("Area ", heron(s1,s2,s3))

main()
