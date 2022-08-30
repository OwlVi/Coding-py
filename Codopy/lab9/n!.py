# n! def

def factortial(n):
    result = 1
    while n>=1:
        result *= n
        n = n-1
    return result
    
n = int(input("Enter n: "))
print(f"{n}!", "=",factortial(n) )