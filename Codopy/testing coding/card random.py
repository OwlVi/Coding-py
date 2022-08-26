#test import randam
import random
card1 = random.randint(1,14)
card2 = random.randint(1,14)
card3 = 0
print(f'P{card1},P{card2}')

if card1 > 10:
    card1 = 10
else:
    card1 = card1
if card2 > 10:
    card2 = 10
else:
    card2 = card2

cardsum = (card1 + card2)%10

if cardsum == 9 :
    print(f'P{cardsum}')
elif cardsum == 8:
    print(f'P{cardsum}')
elif card1 < 4:
    card3 = random.randint(1,14)
    if card3 >= 10:
        card3 = 10
    else:
        pass
    cardsum += card3
    cardsum  = cardsum%10
    print(f'P{card3}') 
print(f'point{cardsum}') 