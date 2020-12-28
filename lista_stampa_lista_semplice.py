matrix = [2, 4, 3, 8,
          9, 3, 2, 7,
          5, 6, 9, 1]
cols = 4
rows = len(matrix)  // cols    

for y in range(rows):
    for x in range (cols):
        v=matrix[y*cols+x]
        print(v, end="\t")
    print()