def product(values: list) -> float:
    if not values:
        return 1
    return values[0]*product(values[1:])
