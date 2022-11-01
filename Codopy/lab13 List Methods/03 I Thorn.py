# THANATHORN
lst = []
n = int(input())
for i in range(n):
    baht = int(input())
    lst.append(baht)
    lst.sort(reverse=True)
money = int(input())
for i in lst:
    x = money//i
    money -= x*i
    print(f'{i}: {x}')

