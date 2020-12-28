matrix = [2, 4, 3, 8,
          9, 3, 2, 7,
          5, 6, 9, 1]
cols = 4
rows = len(matrix)//cols     

for x in range(cols):
    total=0
    for y in range(rows):
        total+=matrix[y*cols+x]