#positive integer

#input
num = int(input(f'Enter positive integer: '))
i = 1
numlk = num # collect value of input
ic = 1
#process
if num <= 0:
    print('Invalid number.') #output
else:
    while True:
        if i == numlk:
            break
        count = 1
        while True:
            count += 1
            if num % count == 0:
                num = num//count
                ic = count
                break
        if numlk%ic ==0:
            print(ic) #output
            i *= ic        

