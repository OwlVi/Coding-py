#digit def

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

n   = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))