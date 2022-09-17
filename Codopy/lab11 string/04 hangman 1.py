# hangman1

guess = input()
n = 0
newguess = []
for i in guess:
    newguess += i
while True:
    s = input()
    if s == '0':
        break
    for i in range(len(newguess)):
        if s == newguess[i]:
            n += 1 
            newguess[i] = ''
            
print(f'{n}/{len(guess)}')
    