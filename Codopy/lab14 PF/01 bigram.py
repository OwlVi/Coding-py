# bigram

text = input().lower()
lst = []
while True:
    if text == '':
        break
    lst.append(text[:2])
    text = text[1:]
lst.sort()
newlst = []
for i in lst:
    if i not in newlst:
        newlst.append(i)
for i in range(len(newlst)):
    if len(newlst[i]) == 2:
        print(newlst[i])


