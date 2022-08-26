#ACME

#input
am = float(input("Enter buying amount: "))

#pocess
# am*0.1 = discount 10% , am*0.15 = discount 15%

#output
if am >= 1000 and am < 3000:
    print("Amount due after discount is {:.2f} baht.".format(am-(am*0.1)))
elif am >= 3000:
    print("Amount due after discount is {:.2f} baht.".format(am-(am*0.15)))
else:
    print("Amount due after discount is {:.2f} baht.".format(am))