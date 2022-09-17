#Count Positive Odd Number

#input

odd = 0 # count odd number
#process
while True :
    num = int(input("Enter number: "))
    if num < 0 :
        break    
    if num % 2 == 1 :
        odd += 1
    
#output
print(f"Received {odd} odd numbers")