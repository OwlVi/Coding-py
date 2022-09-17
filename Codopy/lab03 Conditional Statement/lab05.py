#Guessing
target = 72
#input
gu = int(input("Enter your guess (0 - 100): "))

#output
if gu < 0 or gu >100:
    print("Sorry, out of range, try again later.")
elif gu == target:
    print("Congratulations, your guess is correct.")
else :
    print("Sorry, your guess is wrong, try again later.")