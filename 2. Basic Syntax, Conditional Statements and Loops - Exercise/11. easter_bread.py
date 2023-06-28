budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4

bread_price = flour_price + eggs_price + milk_price

number_of_breads = int(budget // bread_price)

eggs_lost = 0
eggs_left = 0
total_eggs_lost = 0

for eggs in range(1, number_of_breads + 1):
    received_eggs = eggs * 3
    if eggs % 3 == 0:
        eggs_lost = eggs - 2
        total_eggs_lost += eggs_lost

    eggs_left = received_eggs - total_eggs_lost

budget_left = budget - (number_of_breads * bread_price)

print(f"You made {number_of_breads} loaves of Easter bread! Now you have {eggs_left} eggs and {budget_left:.2f}BGN left.")
