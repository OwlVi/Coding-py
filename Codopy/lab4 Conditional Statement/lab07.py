#จับโปเกมอน !!!


#input
lvp = float(input("Enter level pokemon: "))# level pokemon
btl = input("Enter level pokeball: ") # ball tier level
dis = float(input("Enter distance: "))# distance

#process
if btl == 'H' or btl == 'h':
    if 61 <= lvp <= 100 :
        x = 0.01
    if 41 <= lvp <= 60 :
        x = 0.01     
    if 0 <= lvp <= 40 :
        x = 0.01    
elif btl == 'M' or btl == 'm':
    if 61 <= lvp <= 100 :
        x = 0.08
    if 41 <= lvp <= 60 :
        x = 0.05     
    if 0 <= lvp <= 40 :
        x = 0.03
elif btl == 'L' or btl == 'l':
    if 61 <= lvp <= 100 :
        x = 0.1
    if 41 <= lvp <= 60 :
        x = 0.03     
    if 0 <= lvp <= 40 :
        x = 0.05
else:
    x = 0
s = (100)-(lvp*dis*x)
#output
if  0 <= s <= 100:
    print("{:.2f} percent.".format(s))
else:
    s = 0
    print("{:.2f} percent.".format(s))