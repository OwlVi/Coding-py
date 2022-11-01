# sort ped
def check_order(l):
    countx = 0
    county = 0
    x = ''
    for i in range(1,len(l)):
        if l.count(l[i]) == len(l):
            countx += 1
            county += 1
        elif l[i] > l[i-1]:
            countx += 1
        elif l[i] < l[i-1]:
            county += 1

    if countx == 0 and county == 0 and len(l) == 0:
        x = "The list is empty."
    elif countx < county and countx == 0 and countx != len(l):
        x = "The list is in non-increasing order."
    elif countx > county and county == 0 and countx != len(l) :
        x = "The list is in non-decreasing order."
    elif countx == len(l)-1 and county == len(l)-1:
        x = "The list is in non-increasing and non-decreasing order."
    else:
        x = "The list is in random order."
    return x
lst = []
while True:
    i = input('Enter a number (-1 to end): ')
    if i == '-1':
        break
    elif i == '':
        pass
    else:
        i = int(i)
        if i >= 0 and i <= 100:
            lst.append(i)
        else:
            print('Number is out of range.')
print('-'*5)
print('Original list:')
print(lst)
print(check_order(lst))