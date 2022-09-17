# cut in string
num = input()
s = ''
for i in num:
    if i in 'aeiouAEIOU':
        s += ''
    else:
        s += i
print(s)