#Triangle alphabet 2

#input

#process
while True:
    num = int(input("Enter a number: "))
    if num > 26 or num <= 0:
        print(f'Invalid input, program terminates.')
        break
    else:
        while True:
            if num == 0:
                break
            count = 0
            al = '' 
            while count < num:
                al += chr(ord('A')+count)
                count += 1
            num -= 1
            print(al)
        break
#output
