import math

for a in [0, 45, 90, 135]:
    v = math.sin(a * math.pi / 180)
    print(f"Angle: {a:3}; Sin: {v:4.2f}") 
    """
    Nelle {} vengono inserite delle espressioni python.
    3: per dire che gli angoli possono occupare 3 posti;
    4.2f serve per la formattazione di un valore float con due cifre decimali
    e al massimo 4 cifre intere
    """