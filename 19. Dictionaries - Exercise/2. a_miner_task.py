resources_dict = {}

resource = input()

while resource != "stop":
    quantity = int(input())
    if resource not in resources_dict:
        resources_dict[resource] = 0
    resources_dict[resource] += quantity
    resource = input()

for resource, quantity in resources_dict.items():
    print(f"{resource} -> {resources_dict[resource]}")
