#Great Common Divisor: GCD and Least Common Multiplier: LCM

#input
f = int(input(f'Enter the first number: '))
s = int(input(f'Enter the second number: '))
t = 0
ff = f # keep value f
ss = s # keep velue s
lcm = 1# configure
#process
while True:
    gcd = s
    t = s
    s = f%s
    if s == 0:
        lcm = (ff//gcd) * (ss//gcd) 
        lcm = gcd*lcm
        break  
    f = t
#output
print(f'  >> gcd({ff}, {ss}) = {gcd:>6d}')
print(f'  >> lcm({ff}, {ss}) = {lcm:>6d}')