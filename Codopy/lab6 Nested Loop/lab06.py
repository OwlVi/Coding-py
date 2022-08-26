#ผลบวกของหลักเลขจนเหลือหลักเดียว

#input
i = int(input())
s = 0 #set value
sn = 0 # set value sum number
#process
while True:
    while True:
        while True:
            n = i % 10 
            i = i // 10
            s += n
            if i == 0:
                break
        n = s % 10
        s = s // 10
        sn += n
        if s == 0:
            break
    n = sn % 10
    sn = sn // 10
    i += n
    if sn == 0:
        break        
#output
print(i)