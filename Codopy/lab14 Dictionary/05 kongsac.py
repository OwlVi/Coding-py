# bitkub
dic = {}
data = []
n = 0
while True:
    s = input()
    if s == 'end':
        break
    i = s.split()
    if i[0] not in data:
        data.append(i[0])
    if i[0] not in dic:
        dic[i[0]] = [int(i[1])]
    else:
        dic[i[0]] += [int(i[1])]
    if int(i[1]) > n:
        n = int(i[1])
        fw = i[0]
data.sort()

for i in data:
    s = ''
    if len(dic[i]) >= 2:
        s = 's'
    template = f'{i} bid at the price of {max(dic[i]):.1f} baht in {len(dic[i])} time{s}.'
    print(template)

print(f'The winner is {fw}.')