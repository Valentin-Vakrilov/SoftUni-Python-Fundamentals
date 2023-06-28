happiness = list(map(int, input().split(" ")))
happiness_factor = int(input())

updated_happiness = []
total_updated_happiness = 0

for current_happiness in happiness:
    happiness_multiply = current_happiness * happiness_factor
    updated_happiness.append(happiness_multiply)
    total_updated_happiness += happiness_multiply

average_happiness = total_updated_happiness / len(happiness)

happy_employees_counter = 0

for i in updated_happiness:
    if i >= average_happiness:
        happy_employees_counter += 1

if happy_employees_counter >= len(happiness) / 2:
    print(f"Score: {happy_employees_counter}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_employees_counter}/{len(happiness)}. Employees are not happy!")
