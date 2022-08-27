#Craps
target = 0
count = 0
while True:
    count += 1
#input
    x = int(input())
    y = int(input())
#procress
    if (x < 1 or y < 1) or (x > 6 or y > 6):
        count -= 1
        print(f'ERROR')
        continue
    else:
        sxy = x + y
        if (sxy == 7 or sxy == 11 or sxy == target) and count == 1:
            result = "W"
            break
        elif sxy == target:
            result = "W"
            break
        elif (sxy == 2 or sxy == 3 or sxy == 12) and count == 1:
            result = "L"
            break
        elif target != sxy and count == 1:
                target = sxy
        else:
            if sxy == 7 :
                result = "L"
                break
#output
print(f'{count} {sxy} {result}')