quantity = int(input())
days_until_christmas = int(input())
money_spent = 0
christmas_spirit = 0
counter_10th_day = 0
for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        money_spent += 2 * quantity
        christmas_spirit += 5
    if day % 3 == 0:
        money_spent += 8 * quantity
        christmas_spirit += 13
    if day % 5 == 0:
        money_spent += 15 * quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        money_spent += 23
        counter_10th_day += 1
    if counter_10th_day * 10 == days_until_christmas:
        christmas_spirit -= 30
print(f"Total cost: {money_spent}")
print(f"Total spirit: {christmas_spirit}")




