#Buffet

#input
jp = 1000
kn = 1500
#process
# 0.15 = Wednesday receive 15& discount
jpw = jp-(jp*0.15) 
knw = kn-(kn*0.15)

ch = input("Enter your buffet choice: ")
if ch == 'Korean' or ch == 'Japanese':
    we = input("Is today Wednesday (yes/no)? ")
    if ch == 'Japanese':
        b = jp
        if we == 'yes':
            b = jpw
    elif ch == 'Korean':
        b = kn
        if we == 'yes':
            b = knw
    else:
        pass
    print("Your payment is {:.2f} Baht.".format(b))    # b = price buffet 
else:
    print("Sorry, there is no {} buffet.".format(ch))