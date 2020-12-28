class HighScores:
    def __init__(self):
        self._campo=[]*10

    def add(self, p, n):
        self._campo.append((p,n))
        self._campo.sort(reverse=True)
                       

    def print(self):
        for i in self._campo:
            print(i)


def main():
    scores=HighScores()
    punteggio=1
    while punteggio!=0:
        punteggio=int(input("Inserisci un nuovo punteggio:"))
        nome=str(input("Nome del giocatore: "))
        if punteggio!=0 and nome!="":
            scores.add(punteggio, nome)
    scores.print()

main()