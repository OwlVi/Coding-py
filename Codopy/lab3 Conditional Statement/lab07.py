#Calculate f(x)
import math
#input
x = float(input("Enter x : "))

#process
# fw,fa,fs,fd equal
fw = math.ceil(math.sqrt((x**2)+1))
fa = x
fs = (3*math.pow(x,2)) - math.pow((1-x),2)
fd = (2*math.pow(x,3))-(x//math.pow(math.fabs(x)+1,0.5))

#output
if   x < 0 :
    print("f({:.2f}) = {}".format(x,int(fw)))
elif x == 0 :
    print("f({:.2f}) = {}".format(x,int(fa)))
elif x > 0 and x <= 99:
    print("f({:.2f}) = {}".format(x,int(fs)))
elif x > 99 :
    print("f({:.2f}) = {}".format(x,int(fd)))