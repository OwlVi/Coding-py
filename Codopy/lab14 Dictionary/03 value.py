# tanx

valdata = {}
print('Enter variables and values:')
while True:
    val = input()
    if val == '-1':
        break
    val = val.split('=')
    valdata['{'+val[0].strip()+'}'] = val[1].strip()

prodata = []
print('Enter your program:')
while True:
    pro = input()
    if pro == '-1':
        break
    prodata.append(pro)

print('Result:')
for x in prodata:
    for i in valdata:
        x = x.replace(f'{i}' , f'{valdata[i]}')    
    print(x)
