#time change
#input
s1 = int(input("Enter your exercise time 1: "))
s2 = int(input("Enter your exercise time 2: "))
#process
total = s1+s2
h = total//(60*60)
m = (total%(60*60))//60
s = total%60
#output
print("It is", h ,"hours", m ,"minutes and", s ,"seconds.")