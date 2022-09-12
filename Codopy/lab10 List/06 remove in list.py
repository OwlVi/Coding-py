# remove list def

def remove_duplicates(t):    
    data = []
    for x in t:
        if x not in data: 
            data.append(x)
    return data
t = [2, 2, 2, 2, 1, 1, 2, 1, 1, 3, 3, 3]
print(remove_duplicates(t))

