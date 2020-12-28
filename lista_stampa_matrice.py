matrix = [[2, 4, 3, 8],
          [9, 3, 2, 7],
          [5, 6, 9, 1]]
rows = len(matrix)      
cols = len(matrix[0])

y=int(input("row? "))
print(matrix[y])

for y in range(rows):
    for x in range (cols):
        v=matrix[y][x]
        print(v, end="\t")
    print()