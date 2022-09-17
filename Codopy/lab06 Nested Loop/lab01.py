#Master Mind

#input
p1 = int(input('Enter a target (4-digit integer): '))
p2 = int(input('Enter your guess (4-digit integer): '))

pd1 = p1 # collect value 
pd2 = p1 # collect value 

posi = 0 #collect correct position
digi = 0 #collect correct digit

#process
while True:

    p2di = p2 % 10
    while True:
        p1di = p1 %10
        if p2di != 0 and p1di == p2di : #digit num
            digi += 1   
        if p1 < 1:
            p1 = pd1 # return value
            break    
        p1   = p1 //10 # Delete unit digits
    
    p1si = pd2%10 # position
    if p2di != 0 and p1si == p2di :
            posi += 1 
    if p2 < 1:
        digit = digi-posi
        if posi == 0:
            posi = 'No positions'
            if digit == 0:
                digit = 'no digits'
            elif digit == 1:
                digit = 'one digit'
            elif digit == 2:
                digit = 'two digits'
            elif digit == 3 :
                digit = 'three digits'
            elif digit == 4 :
                digit = 'four digits'
        elif posi == 1:
            posi = 'One position'
            if digit == 0:
                digit = 'no digits'
            elif digit == 1:
                digit = 'one digit'
            elif digit == 2:
                digit = 'two digits'
            elif digit == 3 :
                digit = 'three digits'
        elif posi == 2:
            posi = 'Two positions'
            if digit == 0:
                digit = 'no digits'
            elif digit == 1:
                digit = 'one digit'
            elif digit == 2:
                digit = 'two digits'
        elif posi == 3 :
            posi = 'Three positions'
            if digit == 0:
                digit = 'no digits'
            elif digit == 1:
                digit = 'one digit'           
        break
   
    pd2  = pd2 //10 # Delete unit digits
    p2   = p2 // 10 # Delete unit digits
    

#output
if posi == 4:
    print('Congratulations, you just mastered my mind!!')
else:
    print(f'{posi} correct, {digit} correct')