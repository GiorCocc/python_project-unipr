def read(string:str):
    parentesi=False
    for el in string:
        if el=="<":
            parentesi=True
        elif el==">":
            parentesi=False
            print()
        
        if parentesi==True and el!="<":
            print(el, end="")
        
def main():
    string=str(input("Scrivi qualcosa (leggerò solo tra le < >):"))
    read(string)

main()