def long_lines(lista, n:int) -> int:
    count=0
    for i in lista:
        if len(i)>=n:
            count+=1
    return count


def main():
    lista=[]
    s="x"
    n=0
    while s!="":
        s=str(input("Scrivi qualcosa:"))
        lista.append(s)
    n=int(input("Qual'è la soglia? "))
    print("Ci sono", long_lines(lista, n), "righe più lunghe della soglia inserita")

main()