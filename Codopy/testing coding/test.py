I = int(input("Enter level pokemon: "))
b = input("Enter level pokeball: ")
d = int(input("Enter distance: "))

if 0 <= I <= 40 and (b == 'h' or b == 'H') :
    x = 0.01
elif 0 <= I <= 40 and (b == 'm' or b == 'M') :
    x = 0.03
elif 0 <= I <= 40 and (b == 'l' or b == 'L') :
    x = 0.05       

elif 41 <= I <= 60 and (b == 'h' or b == 'H') :
    x = 0.01
elif 41 <= I <= 60 and (b == 'm' or b == 'M')  :
    x = 0.05
elif 41 <= I <= 60 and (b == 'l' or b == 'L') :
    x = 0.03

elif 61 <= I <= 100 and (b == 'h' or b == 'H') :
    x = 0.01
elif 61 <= I <= 100 and (b == 'm' or b == 'M')  :
    x = 0.08
elif 61 <= I <= 100 and (b == 'l' or b == 'L') :
    x = 0.1
else:
    x = 0

result = (100 - (I * d * x))
if 0 < result < 100:
    result = result
else:
    result = 0
print("{:.2f}".format(result) + " percent.")