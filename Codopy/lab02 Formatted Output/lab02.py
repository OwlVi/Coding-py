#Swimming pool
#input
w = float(input("Enter width: "))
l = float(input("Enter length: "))
d = float(input("Enter depth: "))
#process
sq = w*l*d # area
ti = sq*15 # 15 sec
#output
print("Time to fill a pool is","{:.2f}".format(ti/60),"minutes.")