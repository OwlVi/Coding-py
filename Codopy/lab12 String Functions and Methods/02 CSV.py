# CSV NEW

text = input()
x = []
y = ''
word = 0
fword = 0
for i in text:
    if i.isalpha():
        word += 1
    elif i in ' ':
        word += 1
    elif i in ',':
        word += 1
        x.append(text[fword:word])
        fword = word
if text.endswith(','):
    x.append('')
else:
    x.append(text[-1])
for i in range(len(x)) :
    x[i] = x[i].strip(',')
    x[i] = x[i].lstrip()
    x[i] = x[i].rstrip()
for i in range(len(x)):
    y += f'"{x[i]}",'
if y.endswith(','):
    y = y[:len(y)-1]
print(y)