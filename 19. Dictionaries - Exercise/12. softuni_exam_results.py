results_dict = {}
submissions_dict = {}

command = input()

while command != "exam finished":
    current_command = command.split("-")
    user = current_command[0]
    if current_command[1] != "banned":
        language = current_command[1]
        result = int(current_command[2])
        if user not in results_dict:
            results_dict[user] = {language: result}
        elif user in results_dict and language not in results_dict[user]:
            results_dict[user][language] = result
            if result > results_dict[user][language]:
                results_dict[user] = {language: result}
        if language not in submissions_dict:
            submissions_dict[language] = 0
        submissions_dict[language] += 1
    else:
        del results_dict[user]

    command = input()

print("Results:")
for user, language in results_dict.items():
    for language, result in language.items():
        print(f"{user} | {results_dict[user][language]}")
print("Submissions:")
for language, result in submissions_dict.items():
    print(f"{language} - {submissions_dict[language]}")
