def order(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00

    return f"{quantity * price:.2f}"


product_type = input()
quantity_of_product = int(input())

print(order(product_type, quantity_of_product))
