# Blackjack (Easy)
result = []
lst = []
cardsum = 0
n = int(input())
for i in range(n):
    card = input()
    lst.append(card)
for i in range(len(lst)):
    lst[i] = lst[i].split(' ')
    for jqk in lst[i]:
        if jqk in 'A':
            lst[i].insert(lst[i].index('A'), '1')
            lst[i].pop(lst[i].index('A'))
        elif jqk in ' J Q K ':
            lst[i].insert(lst[i].index(jqk), '10')
            lst[i].pop(lst[i].index(jqk))
    for x in range(len(lst[i])):
        cardsum += int(lst[i][x])
        if cardsum <= 16:
            pass
        else:
            break
    if cardsum > 21 :
        result.append('busted')
    else:
        result.append(cardsum)
    cardsum = 0
for i in result:
    print(i)
    