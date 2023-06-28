def odd_and_even_sum(number):
    even_sum = 0
    odd_sum = 0
    for current_digit in str(number):
        current_number = int(current_digit)
        if current_number % 2 == 0:
            even_sum += current_number
        else:
            odd_sum += current_number

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


given_number = input()
print(odd_and_even_sum(given_number))
