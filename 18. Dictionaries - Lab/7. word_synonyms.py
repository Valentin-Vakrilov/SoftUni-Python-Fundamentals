count_of_the_words = int(input())

words_dict = {}

for words in range(count_of_the_words):
    key = input()
    value = input()
    if key not in words_dict:
        words_dict[key] = []
    words_dict[key].append(value)

for key in words_dict:
    print(f"{key} - {', '.join(words_dict[key])}")
