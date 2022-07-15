budget = float(input())
price_kg_flour = float(input())
price_pack_eggs = price_kg_flour * 0.75
price_milk_per_cozonac = price_kg_flour * 1.25 / 4
price_cozonac = price_kg_flour + price_pack_eggs + price_milk_per_cozonac
number_cozonacs = 0
money_spent = 0
number_eggs = 0
lost_eggs = 0
while money_spent <= budget - price_cozonac:
    money_spent += price_cozonac
    number_cozonacs += 1
    number_eggs += 3
    if number_cozonacs % 3 == 0:
        lost_eggs += number_cozonacs - 2
remaining_money = budget - money_spent
remaining_eggs = number_eggs - lost_eggs
print(f"You made {number_cozonacs} cozonacs! Now you have {remaining_eggs} eggs and {remaining_money:.2f}BGN left.")


