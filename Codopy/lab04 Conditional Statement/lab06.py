#leap year

#input
yr  = int(input("Enter year: "))

#process
if  yr < 1:
    print("Invalid year.")
else:
    if yr % 400 == 0 :
        print("{} is a leap year.".format(yr))
    elif yr % 4 == 0 and yr % 100 != 0:
        print("{} is a leap year.".format(yr))
    else:
        print("{} is not a leap year.".format(yr))     