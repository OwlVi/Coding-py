# sum odd
#input
i = int(input())
sn = 0
#process
while True:
    if i == 0 :
        break
    while True:      
        s = i % 10
        if s != 0 and s % 2 != 0:
            sn += s
            break
        else:
            break
            
    i = i // 10
if sn == 0:
    sn = -1
else:
    pass
#output
print(sn)
