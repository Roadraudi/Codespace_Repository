def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

n = int(input("Gib die Anzahl der Fibonacci-Zahlen ein: "))
result = fibonacci(n)
print("Die ersten", n, "Fibonacci-Zahlen sind:", result)
