matrix = []
cols, rows = 0, 0

with open("_matrix.csv", "w") as wfile:
   print("5,7,2,11\n1,6,12,6\n5,6,10,8", file=wfile, end="")

with open("_matrix.csv", "r") as rfile:
    for line in rfile:
        splitted = line.split(",")
        vals = [int(i) for i in splitted]
        # matrix.append(vals)
        # matrix += vals
        col = 0
        for v in vals:
            if v in matrix:
                print(v, rows)
            matrix.append(v)
            col += 1

        cols = len(vals)
        rows += 1

print(rows, "x", cols)
print(matrix)

total = 0
x, y = cols - 1, rows - 1
while x >= 0 and y >= 0:
    total += matrix[y][x]
    x -= 1
    y -= 1
print(total)