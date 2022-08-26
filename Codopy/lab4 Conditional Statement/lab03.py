#Electric Appliance Store

#input
T = int(input("How many TVs? "))
D = int(input("How many DVD players? "))
A = int(input("How many Audio Systems? "))
#process
 # p = price
pt = 6000*T
pd = 1500*D
pa = 3000*A
 # tp = total price
tp = pt + pd + pa

if tp >= 24000:
    d = (tp*0.2) # d = discount 
    print("Total price is {:.2f} baht.".format(tp))
    print("You've got a discount of {:.2f} baht.".format(d))
else:    
    print("Total price is {:.2f} baht.".format(tp))
    d = 0
print("Your payment is {:.2f} baht. Thank you!".format(tp-d))