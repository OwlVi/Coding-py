#Guessing 3 (loop)

#input
target = 72
count = 0 


#process
while True:
    gu = int(input('Enter your guess: '))
    if gu < 0 or gu >100:
        print("Sorry, your guess is out of range.")
    elif gu < target :
        print("Sorry, your guess is too low.")
    elif gu > target :
        print("Sorry, your guess is too high.")    
    count += 1
    if gu == target:
        print('Congratulations, your guess is correct.')
        break
#output    

print(f'Total number of guesses is {count}.')