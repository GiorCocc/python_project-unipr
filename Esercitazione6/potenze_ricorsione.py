def potenza(x:int, n:int):
    if n-1==0:
        return x*1

    x=x*potenza(x,n-1)
    
    return x