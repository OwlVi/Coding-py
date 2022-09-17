#distance

while True:
    go = ''
    #input
    print('<<Point a>>')
    x1 = int(input(f'Enter x coordinate: '))
    y1 = int(input(f'Enter y coordinate: '))
    print('<<Point b>>')
    x2 = int(input(f'Enter x coordinate: '))
    y2 = int(input(f'Enter y coordinate: '))    
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break
    #process
    edis = ((x1-x2)**2+(y1-y2)**2)**0.5
    hdis = abs(x1-x2)
    vdis = abs(y1-y2)     
    if   y2 > y1:
        if x1 == x2:
            go = 'north'
        elif x1 > x2 :
            go = 'north-west'
        elif x2 > x1:
            go = 'north-east'            
    elif y1 > y2 :
        if x2 > x1 :
            go = 'south-east'
        elif x1 == x2 :
            go = 'south'
        elif x1 > x2:
            go = 'south-west'
    elif y1 == y2:
            if  x2 > x1:
                go = 'east'
            elif x1 > x2:
                go = 'west'
            else:
                go = 'nowhere'
#output
    print(f'Distance between ({x1}, {y1}) and ({x2}, {y2}):')
    print(f'Euclidean distance is {edis:.2f}.')
    print(f'Horizontal distance is {hdis}.')
    print(f'Vertical distance is {vdis}.')
    print(f'We are going {go}.')
print(f'Goodbye')
