#Find a, b in which a*b=n and (a+b) is the lowest

#input
n = int(input())
#process
nlk = n
a = 1
i = 0
while a < n:
    b = 1
    while True:
            if b <= n:
                if (a*b == n ) and (a <= b):
                    i = b + a
                    break
            b  += 1 
            if b > n:
                break          
    a += 1
#output
print(i)