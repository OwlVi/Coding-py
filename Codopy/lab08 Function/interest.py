#interest def

def simple_interest(p, r, t):
    simint = p*(r/100)*(t)
    return simint + p

def compound_interest(p, r, t):
    comint = p*(1+(r/100))**(t)
    return comint 

p = int(input("Enter principle: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time: "))    
print('Return money for simple interest calculation is %.2f Baht.' % (simple_interest(p, r, t)))
print('Return money for compound interest calculation is %.2f Baht.' % (compound_interest(p, r, t)))