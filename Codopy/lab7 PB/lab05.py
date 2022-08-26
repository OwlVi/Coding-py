#Prime number checker

#process
while True:
    iii = int(input(f'Enter a number: ')) #input
    if iii == 0:
        print('End of program, goodbye.')
        break
    elif iii <= 1:
        print('Invalid input, try again.')
    else:
        i = 0
        count = 1
        while True:
            if iii % count == 0:
                i +=1
            if count == iii:
                if i > 2 :
                    no1 = ' not'
                    break
                else:
                    no1 = ''
                    break
            count += 1
            
        print(f'{iii} is{no1} a prime number.') #output   
