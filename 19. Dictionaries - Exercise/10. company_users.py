companies_dict = {}

command = input()

while command != "End":
    current_command = command.split(" -> ")
    company = current_command[0]
    employee = current_command[1]
    if company not in companies_dict:
        companies_dict[company] = []
    if employee not in companies_dict[company]:
        companies_dict[company].append(employee)
    command = input()

for company, employee in companies_dict.items():
    print(f"{company}")
    for current_employee in employee:
        print(f"-- {current_employee}")
