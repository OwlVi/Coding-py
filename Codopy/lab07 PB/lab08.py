#Count All Pythagorean AB

#input
c = int(input())
a = 1
count = 0
#process
while a < c:
    b = 1   
    while b <=a:
        if c**2 == b**2 + a**2:
            count += 1
        b += 1
    a += 1
#output
print(count)

