#Summation
#input
print("First fraction:")
a = int(input(">>Enter a numerator a: "))
b = int(input(">>Enter a denominator b: "))
print("Second fraction:")
c = int(input(">>Enter a numerator c: "))
d = int(input(">>Enter a denominator d: "))
#process
x = b*d
y = a*d + c*b 
#output
print("Summation of the two fractions is "+ str(y)+ " / " + str(x))