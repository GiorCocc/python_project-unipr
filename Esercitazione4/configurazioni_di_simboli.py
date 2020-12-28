def config(s:str):
    print("[")
    for i in s:
        for j in s:
            for k in s:
                print('"',i,j,k,'",', end="")
    print("]")

def main():
    lista=["A","E","I","O","U"]
    # for i in range (0,10):        #per utilizzare le cifre
    #     lista.append(i)
    config(lista)

main()