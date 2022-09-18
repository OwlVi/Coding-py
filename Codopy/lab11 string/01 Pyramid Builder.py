# pyramid
num = int(input())
for i in range(0,num):
    print(f'|'+f' '*(num-i-1) + f'*'*i +f'*'+f'*'*i + f' '*(num-i-1) + f'|')