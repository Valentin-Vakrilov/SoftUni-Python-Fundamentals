command = input()

while command != "End":
    if command != "SoftUni":
        doubled_string = ""
        for letter in command:
            doubled_string += letter*2
        print(doubled_string)
    command = input()
