# sunday

def days(d,m):
    for i in range(m): 
        if i in [1,3,5,7,8,10,12]:
            d += 31
        elif i in [4,6,9,11] : 
            d += 30
        elif i in [2]:
            d += 28
    return d

lst = []
xday        = input()
yday        = input()
sundayat    = int(input())
suncount    = 0
result = []
lst.append(xday)
lst.append(yday)

for i in range(len(lst)):
    lst[i] = lst[i].split('-')
    lst[i][i] = int(lst[i][i])
    lst[i][i-1] = int(lst[i][i-1])
    lst[i].reverse()
lst.sort()
print(lst)
start = days(lst[0][1],lst[0][0])
end   = days(lst[1][1],lst[1][0])

print(start , end)
if (lst[0][0] > 12 or lst[1][0] > 12) or (lst[0][0] < 0 or lst[1][0] < 0) :
    result.append('Wrong Month')
if (lst[0][1] > 31 or lst[1][1] > 31) or (lst[0][1] < 0 or lst[1][1] < 0) or (sundayat > 7 or sundayat < 1) :
    result.append('Wrong Day')

for i in range(sundayat,366,7):
    if i >= start and i <= end :
        suncount += 1

if result:
    for i in result:
        print(i)
else:
    print(suncount)