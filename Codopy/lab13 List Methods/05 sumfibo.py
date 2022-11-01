#fibo
def Fibonacci(i):
    count = 0
    x = 1
    y = 1
    lst = []
    while count <= i:
        lst.append(x)
        sn = x+y
        x = y
        y = sn
        count += 1
    return lst

inum    = int(input())
txt     = input()
fibo    = Fibonacci(inum)
result  = 0
if inum >= 0:
    if txt in 'Ee':
        for i in list(range(0,len(Fibonacci(inum)),2)):
            result += fibo[i]
    elif txt in 'Oo':
        if inum != 0:
            for i in list(range(1,len(Fibonacci(inum)),2)):
                result += fibo[i]
        else:
            result = 'ERROR'
    else: 
        result = 'ERROR'
else:
    result = 'ERROR'

print(result)