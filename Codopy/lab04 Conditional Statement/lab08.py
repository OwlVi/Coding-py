#do or not
#input
mbd = float(input("Minutes before due: "))
tem = float(input("Temperature: "))
iir = input("Is it raining (y/n)? ")
#process
day  = (mbd+720)//1440 # 720 =Half day
print(">>> {} days before due.".format(int(day)))        
if  day < 2:
    x = True
elif day > 5:
    x = False
else:
    x = True
    if tem > 25 :
        if iir == 'Y' or iir == 'y':
            x = False 
        else:
            x = True
    elif tem > 40:
            x = False
    else:
            x = True
#output
if x == True :
    print(">>> I will do the assignment.")
else:
    print(">>> I will not do the assignment.")