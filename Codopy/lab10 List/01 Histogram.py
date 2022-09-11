# Histogram 
x = []
for i in range(20):
    x.append(0)
data = []
while True:
    if len(data) == 20:
        break
    scores = int(input('Enter score: '))
    if scores >= 0 and scores <= 10 :
        data.append(scores)
        if 0 == scores:
            x[0] +=  1
        elif 1 == scores:
            x[1] +=  1
        elif 2 == scores:
            x[2] +=  1
        elif 3 == scores:
            x[3] +=  1
        elif 4 == scores:
            x[4] +=  1
        elif 5 == scores:
            x[5] +=  1
        elif 6 == scores:
            x[6] +=  1
        elif 7 == scores:
            x[7] +=  1
        elif 8 == scores:
            x[8] +=  1
        elif 9 == scores:
            x[9] +=  1
        elif 10 == scores:
            x[10] +=  1    
    else:
        print('Score is out of range.')
print("Original list: ")
print(data)
for i in range (11):
    print(f"{i:2.0f}",'*'*(x[i]))