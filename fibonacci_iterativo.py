def fibonacci(n: int) -> int:
    val, nxt = 0, 1

    for i in range(n):
        val, nxt = nxt, val + nxt   #assegnamento multiplo

    return val