# miximaxu

x = input()
y = input()

strx = ''
stry = ''

i = 0
n = 0

for i in range(len(x)):
    if x[i] in 'aeiuo':
       n += 1
    if x[i] in 'aeiou' and n == 2:
       break
    strx += x[i]

    i += 1

for i in range(len(y)) :
    if y[i] in 'aeiou':
        stry = y[i+1:]
        break
    elif y[i] not in 'aeiou':
        stry += y[i]

print(strx+stry)