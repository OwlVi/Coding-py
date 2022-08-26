#01 Is x an Integer?

#input
i = float(input())
#process
integer =  i - int(i) 
if integer == 0 :
    i = f'{i:.0f}'
    n = ''
else:    
    i = f'{i}'
    n = 'not '
#output
print(f'{i} is {n}an integer.')