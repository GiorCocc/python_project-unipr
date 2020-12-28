a=float(input("Parametro a?"))
b=float(input("Parametro b?"))
c=float(input("Parametro c?"))

delta=(b*b)-(4*a*c)

if delta<0:
    print("Nessuna soluzione reale.")
elif delta==0:
    print("Un'unica soluzione reale.")
else:
    print("Due soluzioni reali.")
    
