#january 2

#input
x = input()
n = int(input())
#process
nlk = n # set value n
count = 0
if x == 'Sunday':
    x = 1
elif x == 'Monday':
    x = 2
    n += 2
elif x == 'Tuesday':
    x = 3
    n += 4
elif x == 'Wednesday':
    x = 4
    n += 6
elif x == 'Thursday':
    x = 5
    n += 8
elif x == 'Friday':
    x = 6
    n += 10
elif x == 'Saturday':
    x = 7
    n += 12
else:
    x = 0
if (x > 0 and x <8) and (nlk <= 31 and nlk >=1):
    while True :
        if x > n :
            while True:
                x -= 1
                count += 1
                if x == n:
                    break
        if x == n:
            break
        x += 7
        #print(f'c: {count}')
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
    elif count == 0:
        day = 'Sunday'
else:
    day = ('ERROR')

#output
print(day)
