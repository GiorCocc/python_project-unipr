class Text:
    def __init__(self):
        self._campo=[]

    def add(self, s):
        self._campo.append(s)

    def long_lines(self, n:int) -> int:
        count=0
        for i in self._campo:
            if len(i)>=n:
                count+=1
        return count

def main():
    t=Text()
    s="x"
    n=0
    while s!="":
        s=str(input("Scrivi qualcosa:"))
        t.add(s)
    n=int(input("Qual'è la soglia? "))
    print("Ci sono", t.long_lines(n), "righe più lunghe della soglia inserita")

main()