def f(x):
    return x**3-x-1

def find_zero(x1:float,x2:float)->float:     
    xm=(x1+x2)/2

    # condizione di contratto
    if f(x1)*f(x2)>=0:
        raise ValueError("f non attraversa l'asse")

    #condizione base
    if abs(f(xm))<0.001:
        return xm

    # operazioni da svolgere
    if f(x1)*f(xm)<0:
        return find_zero(x1,xm)
    else:
        return find_zero(xm,x2)