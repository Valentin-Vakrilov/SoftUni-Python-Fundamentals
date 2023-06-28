def operation(a, b, operator):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = a / b
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b

    return result


operation_type = input()
first_number = int(input())
second_number = int(input())

print(int(operation(first_number, second_number, operation_type)))
