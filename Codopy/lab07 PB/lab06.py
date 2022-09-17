#Double rectangle stars

#input
a = int(input(f'Enter height: '))
b = int(input(f'Enter width: '))

#process
if a <= 0 or b <= 0:
    print('Invalid input, program terminates.')
else:
    count = 1 
    while count <= a:
        if count%2 == 0:
            print(' *'*b,end='')
            print()
        else:
            print('* '*b,end='')
            print()
        count += 1
