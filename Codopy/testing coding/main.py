from tabulate import tabulate 
import os
import time
print(" ID:6530200568  นางสาวกฤติมา เชาวน์ดี\n")
choose=''
n = ''
out = 1

#ตารางค่าความจริง
while out:
    print("\tMENU\n 1.Proposition\n 2.Boolean expression\n 3.Exit Program")
    print(" ")
    choose=input("Please Input Number Menu: ")
    os.system('cls')
    if choose == '3':
        print("\tThank you !!\nID:6530200568  นางสาวกฤติมา เชาวน์ดี")
        time.sleep(5)
        break
    elif choose == '1':
        header = ('p','q','r','~r','~q','p/\q','(p/\q)v~r','pv~q','((p/\q)v~r)<->(pv~q)')
        data=[
                ('T','T','T','F','F','T','T','T','T'),
                ('T','T','F','T','F','T','T','T','T'),
                ('T','F','T','F','T','F','F','T','F'),
                ('T','F','F','T','T','F','T','T','T'),
                ('F','T','T','F','F','F','F','F','T'),
                ('F','T','F','T','F','F','T','F','F'),
                ('F','F','T','F','T','F','F','T','F'),
                ('F','F','F','T','T','F','T','T','T'),
                ]
        print(tabulate(data, header , tablefmt='pretty'))
    elif choose == '2':
        header_b = ("w","x","y","z","z'","xw","xz","yz'")
        data_b=[
                ('1','1','1','1','0','1','0','0'),
                ('1','1','1','0','1','1','1','1'),
                ('1','1','0','1','0','1','0','0'),
                ('1','1','0','0','1','1','1','0'),
                ('1','0','1','1','0','0','0','0'),
                ('1','0','1','0','1','0','0','1'),
                ('1','0','0','1','0','0','0','0'),
                ('1','0','0','0','1','0','0','0'),
                ('0','1','1','1','0','0','0','0'),
                ('0','1','1','0','1','0','1','1'),
                ('0','1','0','1','0','0','0','0'),
                ('0','1','0','0','1','0','1','0'),
                ('0','0','1','1','0','0','0','0'),
                ('0','0','1','0','1','0','0','1'),
                ('0','0','0','1','0','0','0','0'),
                ('0','0','0','0','1','0','0','0'),
                ]
        print(tabulate(data_b, header_b , tablefmt='pretty'))
    else:
        print("-"*20)
        print("Try Again !!")
        print("-"*20)
        continue
    time.sleep(5)
    os.system('cls')
    while (1):
        print("{:15}{:>}".format('Go to Main','Enter 1'))
        print("{:15}{:>}".format('Exit Program','Enter 2'))
        n = input("Please Input Number Menu: ")
        if n == '1':
            os.system('cls')
            break 
        elif n=='2':
            os.system('cls')
            print("\tThank you !!\nID:6530200568  นางสาวกฤติมา เชาวน์ดี")
            out = 0
            time.sleep(5)
            break
        else:
            os.system('cls')
            print("Try Again!")
            time.sleep(2)
            os.system('cls')