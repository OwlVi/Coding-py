#Guessing 2
target = 72
#input
gu = int(input("Enter your guess (0 - 100): "))

#process

if gu < 0 or gu >100:
    x ="Sorry, out of range, try again later."
elif gu < target :
    x = "Sorry, your guess is too low, try again later."
elif gu > target :
    x = "Sorry, your guess is too high, try again later."    
else :
    x ="Congratulations, your guess is correct."
#output
print(x)