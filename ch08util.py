def facto(n):
    if n == 0 :
        return 1
    return n * facto(n-1)

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)