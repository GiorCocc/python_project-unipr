r=1
lista=[1,2,3,4,5,6,7,8,9]
def prodotto(lista, r):
    if len(lista) == 0:
        return r

    r*=lista[0]
    
    return prodotto(lista[1:], r)

print("Il prodotto della lista è: ", prodotto(lista, r))