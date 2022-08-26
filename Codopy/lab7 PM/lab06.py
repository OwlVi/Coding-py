#triangle check
#input
a = int(input())
b = int(input())
c = int(input())

#process
if (a > 0 and b > 0 and c > 0):
    if a != b and b != c:
        if (a > c) and (a > b):
            x = a**2
            y = c**2 + b**2
        elif b > a and b > c:
            x = b**2
            y = c**2 + a**2
        else:
            x = c**2
            y = a**2 + b**2
#output
print(x==y)