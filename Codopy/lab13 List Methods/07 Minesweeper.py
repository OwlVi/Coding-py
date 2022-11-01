# bomber man kung
mxn = input()
mxn = mxn.split('x')
for i in range(len(mxn)):
    mxn[i] = int(mxn[i])

databomb = []
n = int(input())
for i in range(n):
    bombpoint = input()
    bombpoint = bombpoint.split(',')
    databomb.append(bombpoint)

for i in range(len(databomb)):
    databomb[i][0] = int(databomb[i][0])
    databomb[i][1] = int(databomb[i][1])
databomb.sort()

mblst = []
for y in range(mxn[0]):
    mblst.append([0]*mxn[1])
for i in range(len(mblst)):
    for x in range(len(databomb)):
        if i+1 == databomb[x][0] or i-1 == databomb[x][0] or i == databomb[x][0]:
            if databomb[x][1] == 0:
                mblst[i][databomb[x][1]] += 1
                mblst[i][databomb[x][1]+1] += 1
            elif databomb[x][1]+1 == mxn[1]:
                mblst[i][databomb[x][1]-1] += 1
                mblst[i][databomb[x][1]] += 1
            else:
                mblst[i][databomb[x][1]-1] += 1
                mblst[i][databomb[x][1]] += 1
                mblst[i][databomb[x][1]+1] += 1

for i in range(len(mblst)):
    for x in range(len(databomb)):
        if i == databomb[x][0]:
            mblst[i][databomb[x][1]] = '*'

for i in mblst:
    txt = ''
    for x in i:
        txt += str(x)
    print(txt)