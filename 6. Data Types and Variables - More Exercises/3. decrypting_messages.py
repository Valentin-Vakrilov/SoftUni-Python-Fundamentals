key = int(input())
number_of_lines = int(input())

message = []

for symbol in range(number_of_lines):
    current_symbol = input()
    new_symbol = chr(ord(current_symbol) + key)
    message.append(new_symbol)

print("".join(message))
