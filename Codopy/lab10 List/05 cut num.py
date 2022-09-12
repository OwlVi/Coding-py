# sort number

x = 0
nsort = []
while True:
    num = int(input())
    if num == -1:
        break
    if num > x :
        x = num
        nsort.append(num)
print(nsort)
        