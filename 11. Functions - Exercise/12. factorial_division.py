def factorial(some_number):
    result = some_number
    for number in range(some_number-1, 1, -1):
        result *= number

    return result


first_number = int(input())
second_number = int(input())

divided_result = factorial(first_number) / factorial(second_number)
print(f"{divided_result:.2f}")
