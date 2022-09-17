#input
iii = int(input(f'Enter a number: '))
cou = 0
res = 1
fac = '1'
#process
while True:
    if iii < 0:
        print(f'Invalid input, program terminates.')
        break
    else:
        if cou > iii:
            break
        while True:
            if cou < 2:
                break
            else:
                res *= cou
                fac = f'{cou} x ' + fac
                break
        print(f'{cou}! = {fac} = {res}')
        cou += 1