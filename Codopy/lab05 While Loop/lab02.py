#parking (harder)
import math
hours = int(input('Enter number of hours (0-20): '))
minutes = int(input('Enter number of minutes (0-59): '))
buyAmt = int(input('Enter shopping amount: '))
import math
#process
hrs = hours + (math.ceil(minutes/60)) #target
if (hours < 0 or hours > 20) or (minutes < 0 or minutes >= 60) or hrs > 20:
        x = "Invalid time."
else:
    x = ''
    ba = 0
    count = 0
    while True:
        if count > hrs:
            break
        elif count <= 2:
            pass
        elif count >= 3 and count <= 4:
            ba = ba + 20
        elif count >= 5:
            ba = ba + 50 
        count += 1
    if buyAmt > 3000:
            ba = 0
    elif buyAmt <= 3000 and buyAmt >= 300  :
            ba -= 20
            if hrs >= 4 :
                ba -= 20
    else:
        ba = ba
    if ba == 0 :
        x = (f"No charge, thank you.")
    else:
        x = (f"Total amount due is {ba} Baht, thank you.")
#output
print(x)