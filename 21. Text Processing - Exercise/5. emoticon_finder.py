text = input()

for char in range(len(text)):
    if text[char] == ":":
        emoticon = [text[char], text[char+1]]
        print("".join(emoticon))
