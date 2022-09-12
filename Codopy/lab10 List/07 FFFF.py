#No more test

#input
tfex = int(input())     # total of ex
perr = float(input())   # percent success
nofn = int(input())     # nisit
data = [] # data base pass
noff = 0 # number of fail

#process
for i in range(nofn):
    dfex = int(input())
    if (dfex/tfex)*100 < perr:
        noff += 1
    data += [(dfex/tfex)*100]

#output
print(noff)
for i in range(nofn):
    if data[i] < perr:
        print(f'({i+1}) {data[i]:.2f}')
    else:
        print(f'{i+1} {data[i]:.2f}')

