#hang hang man

guess = input()
nguess = []

for i in guess:
    nguess += '-'
    
while True:
    s = input()
    if s == '0':
        break
    for i in range(len(nguess)):
        if s == guess[i]:
            nguess[i] = s

cguess = ''
for i in nguess:
    cguess += i

print(cguess)
    