# IN MY HEART

rlst = []
llst = []

#Input
while True:
    text = input()
    if text == '-1':
        break
    text = text.split("=",1)
    rlst.append(text[1].strip())
    llst.append(text[0].strip())
x = 0
for i in range(len(llst)) :
    if len(llst[i]) > x:
        x = len(llst[i])
#Output
for i in range(len(llst)):
    print(llst[i].rjust(x),"=",rlst[i])
