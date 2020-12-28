from functools import lru_cache

@lru_cache()                   # function decoration #tecnica della memoisation, crea una lista per i risultati della funzione pura di fibonacci
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


#come diventa la funzione con la notazione lru_cache

# @lru_cache

# _fibonacci_lookup = [0, 1]

# def fibonacci(n: int) -> int:
#     if n < len(_fibonacci_lookup):
#         return _fibonacci_lookup[n]
#     result = fibonacci(n - 1) + fibonacci(n - 2)
#     _fibonacci_lookup.append(result)
#     return result