numbers_sequence = input().split()
text = input()

message = []

for number in numbers_sequence:
    index_sum = 0
    for index in number:
        current_index = int(index)
        index_sum += current_index
    if index_sum > len(text):
        searched_index = index_sum - len(text)
    else:
        searched_index = index_sum
    symbol = text[searched_index]
    message.append(symbol)
    text = text[:searched_index] + text[searched_index+1:]

print(''.join(message))
