happiness = input().split(" ")
happiness_factor = int(input())

multiplied_happiness = list(map(lambda x: int(x) * happiness_factor, happiness))

filtered_happiness = list(filter(lambda x: x >= sum(multiplied_happiness) / len(multiplied_happiness), multiplied_happiness))

if len(filtered_happiness) >= len(multiplied_happiness) / 2:
    print(f"Score: {len(filtered_happiness)}/{len(multiplied_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_happiness)}/{len(multiplied_happiness)}. Employees are not happy!")
