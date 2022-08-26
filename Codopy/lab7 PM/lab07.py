#january

#input
x = int(input())
n = int(input())
#process
if x > 7 or x < 1 or n < 1 or n > 31:
    day = 'ERROR'
else:
    count = 0
    while True:
        if x > n :
            while True:
                x -= 1
                count += 1
                if x == n:
                    break
        if  x == n:
            break
        x += 7 # week    
    
    if count == 1:
        day = 'Saturday'
    elif count == 2:
        day = 'Friday'
    elif count == 3:
        day = 'Thursday'
    elif count == 4:
        day = 'Wednesday'
    elif count == 5:
        day = 'Tuesday'    
    elif count == 6:
        day = 'Monday'
    else:
        day = 'Sunday'
#output
print(day)