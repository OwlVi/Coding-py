#Alternating Sum def

def alternaing_sum(n):
    altsum = 0
    count = 1
    while count <= n:
        if count % 2:
            altsum += count
        else:
            altsum -= count
        count += 1
    return altsum

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n,alternaing_sum(n)))
