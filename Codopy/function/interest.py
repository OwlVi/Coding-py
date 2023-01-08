#interest def

def simple_interest(p, r, t):
    simint = p*(r/100)*(t)
    return simint + p

def compound_interest(p, r, t):
    comint = p*(1+(r/100))**(t)
    return comint 
