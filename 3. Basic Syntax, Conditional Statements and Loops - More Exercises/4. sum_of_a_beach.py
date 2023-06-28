given_string = input().lower()

total_counter = given_string.count('sand') + given_string.count('water') + given_string.count('fish') +\
                given_string.count('sun')

print(total_counter)
