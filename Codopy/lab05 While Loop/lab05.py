#Triangle of 1s

#input
a = int(input("Enter height: "))
i = 0
a -= 1
#process
while True :
    if i == a+1:
        break
    if i == 0:
        print("  "*(a-i)+f"1")
    else:
        print("  "*(a-i)+f"1"+" "*((4*i)-1)+f"1")
    i += 1