# count in string

num = input()
s = ''
n = 0
for i in num:
    if i in 'aeiouAEIOU':
        n += 1
print(n)