def limit_values(values, max_val):
    # procedure: process data, no direct result
    for i in range(len(values)):
        if values[i] > max_val:
            values[i] = max_val

    # the pythonic way: for i, val in enumerate(values): ...

def main ():
    data = [5, 4, 2]
    limit_values(data, 4)
    print(data)

main()