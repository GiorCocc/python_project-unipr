def factorial(n: int) -> int:
    result = 1
    if n > 0:
        result = n * factorial(n - 1)
    return result

f=factorial(9)
print(f)