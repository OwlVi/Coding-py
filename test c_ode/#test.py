#test
import random

money_start = int(input("give me a money : "))
ran_numf = random.randint(1,11)
rounds = 1

while money_start <= 0 and rounds == 5:
    print(f"round : {rounds}")
    print(f"money : {money_start}")
    print(f"number : {ran_numf}")
    gress_ml = input(f" m or l | {money_start} : ")
    money_bet = int(input("bet : "))
    ran_nums = random.randint(1,11)
    if ran_nums == ran_numf :
        money_start = money_start
    elif (ran_nums > ran_numf) and gress_ml == 'm' :
        money_start = money_start+money_bet
    elif (ran_nums < ran_numf) and gress_ml == 'l' :
        money_start = money_start+money_bet
    else:
        money_start = money_start-money_bet
    ran_numf = ran_nums
    rounds += 1
if rounds < 5 :
    print("You lose")
else:
    print(money_start)
    