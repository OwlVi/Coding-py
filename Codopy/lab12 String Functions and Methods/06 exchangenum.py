#how to exchange

#input

txtnum = input()
x = True
if '.' in txtnum:
    if ',' not in txtnum:
        txtindot = txtnum.rsplit('.')
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
        txtdot = txtnum.rsplit('.')
        if len(txtdot[-1]) < 3:
            txtcomma = txtdot[0].split(',')
            if len(txtcomma[0]) <= 3 and len(txtcomma[0]) >= 1 and txtcomma[0].isdigit():
                txtdot[0] = txtdot[0].replace(',','')
                if len(txtcomma[-1]) == 3  and txtcomma[-1].isdigit() :
                    for i in range(1,len(txtcomma)-1):
                        if len(txtcomma[i]) == 3 and txtcomma[i].isdigit():
                            pass
                        else:
                            x = False
                            break
                    if x:
                        print(f'{int(txtdot[0])+1}.{txtdot[-1]}')
                    else:
                        print('ERROR')
                else:
                    print("ERROR")
        
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