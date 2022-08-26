#Triangle alphabet 3

#input

#process
while True:
    num = int(input("Enter a number: "))
    if num > 26 or num <= 0:
        print(f'Invalid input, program terminates.')
        break
    else: 
        count = 0
        al = '' 
        while count < num:
            al += chr(ord('A')+count)
            print(al)
            count += 1 
        while True:  
            if num == 1:
                break
            num -= 1
            count = 0
            al = ''
            while count < num:
                al += chr(ord('A')+count)
                count += 1
            print(al)
        break
#output
