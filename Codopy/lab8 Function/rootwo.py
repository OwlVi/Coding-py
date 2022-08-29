#root def

def sqrt_n_times(a,b):
    count = 1
    while count <= b:
        count += 1
        a = a**0.5
    return a

x = float(input())
n = int(input())
print(sqrt_n_times(x, n))