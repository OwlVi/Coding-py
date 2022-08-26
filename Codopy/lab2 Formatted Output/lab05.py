#fill fuel
#input
dis  = int(input())
fue  = int(input())
#process
a = (fue*0.5)*15 # use 50% of tank  //  15 kilometer per lit
b = (fue*0.9)*15 # use 90% of tank //   15 kilometer per lit
x = int(dis//a)+1 # +1 = First fill
y = int(dis//b)+1
#output
print(x)
print(y)
