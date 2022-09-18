# elab

text = input()
lst = []
for i in text :
    if i not in '[]':
        lst += i
gues = input()
count = 0
for i in text:
    if i in gues :
        count += 1
if lst :
    print(count)
    print(f'{(count/len(lst))*100:.2f}')
else:
    print(count)
    print(f'{(count)*100:.2f}')
