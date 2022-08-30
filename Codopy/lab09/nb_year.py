# bal-e def

def nb_year(p0, percent, aug, p):
    day = 0
    while p0 < p:
        day += 1 
        p0 = int(p0 + (p0*(percent/100)) + aug)
    return day

print( nb_year(1000, 2, 30, 1150) )