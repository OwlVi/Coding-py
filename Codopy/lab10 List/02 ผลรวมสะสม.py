#Accumulative Sum
def accum_sum(l):
    x = 0
    print('Accumulative Sum: ')
    for i in range(len(data)):
        x += data[i] 
        print(x) 
    return
data = []
while True:
    num = int(input("Enter a number (0 to end): "))
    if num == 0:
        break
    if num > 0 and num < 1000:
        data.append(num)
    else: 
        print("Number is out of range. ")
print("Original list: ")
print(data)
accum_sum(data)
