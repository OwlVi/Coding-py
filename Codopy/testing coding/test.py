#how to exchange

#input

txtnum = input()
x = True
if '.' in txtnum:
    if ',' not in txtnum:
        txtindot = txtnum.split('.')
        for i in txtindot:
            if i.isdigit() and len(txtindot[-1]) < 3:
                pass
            else:
                x = False
                break
        if x:
            print(f'{int(txtindot[0])+1}.{txtindot[-1]}')
        else:
            print('ERROR')
    else:
        chcoma = txtnum.split(',')
        txtindot = chcoma[-1].split('.')
        if len(txtindot[0]) == 3:
            txtnum = txtnum.replace(',','')        
            txtindot = txtnum.split('.')
            for i in txtindot:
                if i.isdigit() and len(txtindot[-1]) < 3:
                    pass
                else:
                    x = False
                    break
            if x:
                print(f'{int(txtindot[0])+1}.{txtindot[1]}')
            else:
                print('ERROR')
        else:
            print('ERROR')
elif ',' in txtnum:
    txtcomma = txtnum.split(',')
    for i in range(1,len(txtcomma)):
        if txtcomma[0].isdigit() and txtcomma[i].isdigit() and len(txtcomma[i]) == 3 and len(txtcomma[i]) <= 3:
            pass
        else:
            x = False
            break
    if x:
        print(int(txtnum.replace(',',''))+1)
    else:
        print('ERROR')
else:
    if txtnum.isdigit():
        print(int(txtnum)+1)
    else:
        print('ERROR')