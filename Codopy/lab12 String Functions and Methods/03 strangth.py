# IN MY HEART

rlst = []
llst = []

#Input
while True:
    txt = input()
    if txt == '-1':
        break
    lst = []
    word = 0
    fword = 0
    for i in txt:
        if i.isalnum():
            word += 1
            continue
        elif i in ' ':
            word += 1
            continue
        elif i in f'=' and fword == 0:
            word += 1
            lst.append(txt[fword:word-1].strip())
            fword = word
    lst.append(txt[fword:len(txt)].strip())
    
    rlst.append(lst[1].strip())
    llst.append(lst[0].strip())
    
x = 0
for i in range(len(llst)) :
    if len(llst[i]) > x:
        x = len(llst[i])
#Output
for i in range(len(llst)):
    print(llst[i].rjust(x),"=",rlst[i])
