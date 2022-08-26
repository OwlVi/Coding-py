#print digit

#input
a = 0 # take value
n = int(input())
count = 0
#process
if n > 0:
    while True:
        x = 10**(count+1) # pow(10,count)
        a = ((n%x)-a)//10**count
        if n-10**count <= 0 :
            break          
        print(a)
        count += 1
else:
    print("ERROR")