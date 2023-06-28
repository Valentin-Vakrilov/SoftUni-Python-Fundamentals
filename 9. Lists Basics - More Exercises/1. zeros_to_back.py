string = list(map(int, input().split(", ")))

for digit in string:
    if digit == 0:
        string.remove(digit)
        string.append(digit)

print(string)
