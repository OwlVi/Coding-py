
def digit(n):
    n = n % 10
    return n

def tens(n):
    n = n // 10
    n = n % 10
    return n

def hundreds(n):
    n = n // 100
    n = n % 10
    return n

def thousands(n):
    n = n // 1000
    return n

def sum_digits(n):
    n = digit(n) + tens(n) + hundreds(n) + thousands(n)
    return n
