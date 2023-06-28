current_version = [int(number) for number in input().split(".")]

current_version[-1] += 1

for current_index in range(len(current_version) - 1, -1, -1):
    if current_version[current_index] > 9:
        current_version[current_index] = 0
        current_version[current_index - 1] += 1

print('.'.join(str(number) for number in current_version))

# current_version = input()
#
# current_version_as_int = int(current_version.replace(".", ""))
#
# new_version = current_version_as_int + 1
#
# new_version_as_str = str(new_version)[0] + "." + str(new_version)[1] + "." + str(new_version)[2]
#
# print(new_version_as_str)
