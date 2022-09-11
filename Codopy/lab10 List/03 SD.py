# SD
def find_sd(l):
    x = 0
    for i in range(len(l)):
        x += (l[i]-(sum(l)/len(l)))**2
    sd = (x/(len(l)-1))**0.5
    return sd
datascore = []
while True:
    score = float(input('Enter score: '))
    if score == -1:
        break    
    if score >= 0 and score <= 100:
        datascore.append(score)
    else:
        print('Score is out of range.')

if datascore:
    print(f"Maximum score is {max(datascore):.2f}.")
    print(f"Minimum score is {min(datascore):.2f}.")
    print(f"Average score is {sum(datascore)/len(datascore):.2f}.")
    print(f'Standard deviation is {find_sd(datascore):.2f}.')
