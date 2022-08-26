#rule of 9

#input
nm = int(input())
a = 0 # set value
while True:
    if nm == 0:
        break
    a += (nm%10)
    nm = (nm//10)    

if a % 9 == 0:
    sa = a
    print(f'Yes {sa}')    
else:
    sa = a % 9
    print(f'No {sa}') 
