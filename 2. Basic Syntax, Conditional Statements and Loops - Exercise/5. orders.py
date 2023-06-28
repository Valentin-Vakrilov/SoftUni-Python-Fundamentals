number_of_orders = int(input())

total_orders = 0

for order in range(0, number_of_orders):
    capsule_price = float(input())
    number_of_days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= capsule_price <= 100 and 1 <= number_of_days <= 31 and 1 <= capsules_per_day <= 2000:
        price_of_order = capsules_per_day * capsule_price * number_of_days
        print(f"The price for the coffee is: ${price_of_order:.2f}")
        total_orders += price_of_order
    else:
        continue

print(f"Total: ${total_orders:.2f}")
