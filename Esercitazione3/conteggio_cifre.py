def conta_zero(s):
    count=0
    for i in s:
        if i=="0":
            count+=1
    return count

def main():
    string=str(input("Dammi una serie di valori:"))
    c=conta_zero(string)
    print("Nella frase ci sono ", c, "zeri")

main()