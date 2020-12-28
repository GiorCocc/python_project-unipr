matrix = [[2, 4, 3, 8],
          [9, 3, 2, 7],
          [5, 6, 9, 1]]
rows = len(matrix)      
cols = len(matrix[0])

x=int(input("cols? "))
total=0

for y in range(rows):
    total+=matrix[y][x]         #per le matrici devo lavorare con due indici, uno per la riga e uno per la colonna

print(total)

for x in range(cols):
    total=0
    for y in range(rows):
        total+=matrix[y][x]