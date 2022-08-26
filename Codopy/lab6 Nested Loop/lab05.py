#building i cant see

#input
t = 0
n = 0
#process
while True:
    i = int(input())
    if t < i:
        t = i
        n += 1     
    if i == -1:
        break
#output
print(n)