#menu

print("---<< Main Menu >>---")
print("{:>7s}urger Meal".format("<B>"))
print("{:>7s}hicken Meal".format("<C>"))
print("{:>7s}asta Meal".format("<P>"))
main = input("Enter your choice: ")

if main == 'B' or main == 'b':
    print("---<< Burger Sub Menu >>---")
    print("{:>7s}egular Burger".format("<R>"))
    print("{:>7s}heese Burger".format("<C>"))
    print("{:>7s}ouble Cheese Burger".format("<D>"))    
    sub = input("Enter your choice: ")
    if sub == 'R' or sub == 'r':
        print("Your Regular Burger is 60 Baht.")
    elif sub == 'C' or sub == 'c':
        print("Your Cheese Burger is 75 Baht.")
    elif sub == 'D' or sub == 'd':
        print("Your Double Cheese Burger is 90 Baht.")
    else:
        print("Invalid sub menu choice.")
        
elif main == 'C' or main == 'c':
    print("---<< Chicken Sub Menu >>---")
    print("{:>7s}ried Chicken".format("<F>"))
    print("{:>7s}rilled Chicken".format("<G>"))
    print("{:>7s}hef's Chicken".format("<C>"))    
    sub = input("Enter your choice: ")
    if sub == 'F' or sub == 'f':
        print("Your Fried Chicken is 120 Baht.")
    elif sub == 'G' or sub == 'g':
        print("Your Grilled Chicken is 150 Baht.")
    elif sub == 'C' or sub == 'c':
        print("Your Chef's Chicken is 180 Baht.")
    else:
        print("Invalid sub menu choice.")
        
elif main == 'P' or main == 'p':
    print("---<< Pasta Sub Menu >>---")
    print("{:>7s}paghetti de Italiano".format("<S>"))
    print("{:>7s}asagna Supreme".format("<L>"))
    print("{:>7s}acaroni Special".format("<M>"))    
    sub = input("Enter your choice: ")
    if sub == 'S' or sub == 's':
        print("Your Spaghetti de Italiano is 90 Baht.")
    elif sub == 'L' or sub == 'l':
        print("Your Lasagna Supreme is 120 Baht.")
    elif sub == 'M' or sub == 'm':
        print("Your Macaroni Special is 100 Baht.")
    else:
        print("Invalid sub menu choice.")
else:
    print("Invalid main menu choice.")