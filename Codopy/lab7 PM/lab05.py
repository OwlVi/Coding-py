#number in integer
#input
number = int(input(f'Enter a number: '))
digit  = int(input(f'Enter a digit: '))
occurs = 0 # set value
s      = 's'
if number < 0:
    print(f'Invalid number.')
    if digit > 9 or digit < 0:
            print(f'Invalid digit.')
else:
    if digit > 9 or digit < 0:
        print(f'Invalid digit.')
    else:
        while number > 0 :
            if digit > 9 or digit < 0:
                print(f'Invalid digit.')
                break
            i = number%10
            number = number//10
            if i == digit:
                occurs += 1
                if occurs == 1:
                    s = ''
                else:
                    s = 's'
#output
        print(f'Digit {digit} occurs {occurs} time{s}.')
