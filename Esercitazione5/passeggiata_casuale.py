from random import randint

def main():
    x=0
    y=0
    n=int(input("Dammi il numero di passi da compiere:"))
    with open("passeggiata.txt","w") as passeggiata:
        for i in range (n):
            r=randint(0,3)
            if r==0:
                y-=1
            elif r==1:
                x+=1
            elif r==2:
                y+=1
            elif r==3:
                x-=1
            print(r,",",x,",", y, file=passeggiata)
main()