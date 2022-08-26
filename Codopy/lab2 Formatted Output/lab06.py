#print star 2
#input
n = int(input())
a = input()
b = input()
#process
result = f'{(a+b)*n//2}'+ a*(n%2) # %2 when is even number
#output
print(result)