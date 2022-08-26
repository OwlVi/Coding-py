#function math
import math
#input
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

#process
a1 = math.pow(x,y)+z
a2 = math.cos(2*(math.pi)) + math.log(x,math.e)
a3 = math.fabs(x)+math.fabs(y)
a4 = math.sqrt((x**2)+(y**2)+(z**2))
a5 = math.sin(x)**2 + math.cos(x)**2
a6 = math.pow((x+y),(1/5))
a7 = math.e**(x*math.log(y,math.e))
#output

print("a1 = {:.2f}".format(a1))
print("a2 = {:.2f}".format(a2))
print("a3 = {:.2f}".format(a3))
print("a4 = {:.2f}".format(a4))
print("a5 = {:.2f}".format(a5))
print("a6 = {:.2f}".format(a6))
print("a7 = {:.2f}".format(a7))