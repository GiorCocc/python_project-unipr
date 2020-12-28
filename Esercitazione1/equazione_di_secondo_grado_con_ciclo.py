from math import sqrt

scelta="s"

while scelta=="s":
    a=float(input("Parametro a?"))
    b=float(input("Parametro b?"))
    c=float(input("Parametro c?"))

    delta=(b*b)-(4*a*c)

    if delta<0:
        print("Nessuna soluzione reale.")
    elif delta==0:
        x1=(-b-sqrt(delta))/2*a
        print("Un'unica soluzione reale che è:", x1)
    else:
        x1=(-b-sqrt(delta))/2*a
        x2=(-b+sqrt(delta))/2*a
        print("Due soluzioni reali che sono:",x1,",",x2)
        
    scelta=input("Vuoi controllare un'altra equazione di secondo grado? (s/n)")
    
    
