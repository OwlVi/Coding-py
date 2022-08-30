#Fibo def 

def Fibonacci(n):
    count = 1
    x = 1
    y = 1
    sn = 1
    while count < n-1:
        sn = x+y
        x = y
        y = sn
        count += 1
    return sn      

n = int(input("Enter n: "))
print("fibo({}) = {}".format(n,Fibonacci(n)))

