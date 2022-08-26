#mowing cost
#input
bl = int(input("Enter block length: "))
bw = int(input("Enter block width: "))
hl = int(input("Enter house length: "))
hw = int(input("Enter house width: "))
#process
blong = bl*bw
hlong = hl*hw
area = blong >= hlong
x = ((blong*area)-(hlong*area))*35
#output
print("Mowing cost is",x,"baht.")
