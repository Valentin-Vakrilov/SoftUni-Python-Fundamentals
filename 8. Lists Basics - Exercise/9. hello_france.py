items = input().split("|")
budget = float(input())

train_ticket = 150

items_with_new_prices = []
final_prices = ""

current_budget = budget
profit = 0

for item in items:
    new_price_of_item = 0
    splitting_item = item.split("->")
    current_item = splitting_item[0]
    current_item_price = float(splitting_item[1])
    if current_budget >= current_item_price:
        if current_item == "Clothes" and current_item_price <= 50:
            current_budget -= current_item_price
            new_price_of_item += current_item_price * 1.4
            items_with_new_prices.append(new_price_of_item)
            profit += new_price_of_item - current_item_price
        elif current_item == "Shoes" and current_item_price <= 35:
            current_budget -= current_item_price
            new_price_of_item += current_item_price * 1.4
            items_with_new_prices.append(new_price_of_item)
            profit += new_price_of_item - current_item_price
        elif current_item == "Accessories" and current_item_price <= 20.50:
            current_budget -= current_item_price
            new_price_of_item += current_item_price * 1.4
            items_with_new_prices.append(new_price_of_item)
            profit += new_price_of_item - current_item_price

for current_price in items_with_new_prices:
   new_price = f"{current_price:.2f}"
   final_prices += new_price + " "

print(final_prices)
print(f"Profit: {profit:.2f}")

if budget + profit >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
