#bowling

#input
count = 1
score = 0
#process
while True:
    if count == 11:
        break    
    print(f'Frame # {count}')
    i = int(input(f'  Number of pins down: '))
    if i == 10: # strike
        score += 10
        count += 1
    elif i < 10:
        score += i # open frame
        i = 10-i
        print(f'Frame # {count}')
        it = int(input(f'  Number of pins down (0-{i}): '))
        if it >= 0 and it <= i: # spare when value = i
            score += it
        count += 1
#output
print(f'Total score is {score}')
    