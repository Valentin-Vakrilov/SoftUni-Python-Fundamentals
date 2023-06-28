text = input().split()

total_sum = 0

for current_string in text:
    first_letter = current_string[0]
    last_letter = current_string[-1]
    number = int(current_string[1:-1])
    result = 0
    if first_letter.isupper():
        result += number / (ord(first_letter) - 64)
    else:
        result += number * (ord(first_letter) - 96)
    if last_letter.isupper():
        result -= ord(last_letter) - 64
    else:
        result += ord(last_letter) - 96

    total_sum += result

print(f"{total_sum:.2f}")
