file_path = input().split("\\")

searched_subtract = file_path[-1]

splitted_searched_subtract = searched_subtract.split(".")

file_name = splitted_searched_subtract[0]
file_extension = splitted_searched_subtract[1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
