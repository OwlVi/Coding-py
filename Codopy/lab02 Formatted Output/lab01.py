#import math
import math
#input
r = abs(int(input("Enter a radius: ")))
#process
area = math.pi*(r**2)
cir = math.pi*(r)*2
#output
print("Area of a circle with radius",r,"{:3s}{:.2f}".format("is",area))
print("Circumference of a circle with radius",r,"{:3s}{:.2f}".format("is",cir))
