def palindrome_check(numbers_list):
    result = ""
    for number in numbers_list:
        is_palindrome = number[0] == number[-1]
        result += str(is_palindrome) + '\n'
    return result[0:-1]


numbers = input().split(", ")

print(palindrome_check(numbers))
