budget = int(input())
command = input()

total_prices = 0
while command != "End":
    price = int(command)
    total_prices += price
    if budget < total_prices:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")