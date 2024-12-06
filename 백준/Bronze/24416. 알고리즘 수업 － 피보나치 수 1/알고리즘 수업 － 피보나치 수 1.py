n = int(input())

def fib(n):
    a, b = 1, 1 # f(1), f(2)
    for _ in range(3, n + 1): 
        a, b = b, a + b

    return b

def fibonacci(n):
    return n - 2

print(fib(n), fibonacci(n))