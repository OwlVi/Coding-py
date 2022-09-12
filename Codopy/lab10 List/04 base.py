# find mode
xda = [0]*11

def find_mode(l):
    print('Mode of scores: ')
    for x in range(11):
        for i in range(20):
           if x == l[i]:
             xda[x] += 1
    for i in range(11):
        if xda[i] == max(xda):
            print(i)
    return
dscores = []
while True:
    if len(dscores) == 20:
        print('-'*5)
        break
    scores = int(input("Enter score: "))
    if scores >= 0 and scores <= 10:
        dscores.append(scores)
    else:
        print('Score is out of range.')
if dscores :
    print('Original list: ')
    print(dscores)
    find_mode(dscores)