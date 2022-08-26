#negative income tax

#input
age = int(input("Enter your age: "))
inc = int(input("Enter your net income: "))

if   14 < age  <= 60 :
    if 0 < inc < 30000  :
        nit = inc*0.2
        print("Your negative income tax is {:.2f} Baht.".format(nit))
    elif 30000 <= inc < 80000:
        nit = 6000-(inc-30000)*(0.12) # 6000 is income 30000 * 0.2 
        print("Your negative income tax is {:.2f} Baht.".format(nit))
    else:
        print("Invalid income.")      
    
else:
   print("Invalid age.") 
