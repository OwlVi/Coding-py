# parking
import math

#input
# ho = hour , mi = minutes

ho = int(input("Enter number of hours: "))
mi = int(input("Enter number of minutes: "))

#pocess
# yo = parking fee
# ((ho*10)-10)|  2 hour
# (math.ceil(mi/60)*10)| ceil number to integer
# ((ho*10)-10)+(math.ceil(mi/60)*10)

#output
if ho < 0 or mi < 0 or mi > 59: # check error
    print("Input Error!") 
elif ho >= 0 and ho < 2 and mi <= 15: # min 16
    print("No charge, thanks.")
elif ho >= 0 and ho < 2 and mi >= 0 and mi <=59: # in 2 hour
    print("Total amount due is 10 Bahts.")
else:
    print("Total amount due is {} Bahts.".format(((ho*10)-10)+(math.ceil(mi/60)*10)))    
