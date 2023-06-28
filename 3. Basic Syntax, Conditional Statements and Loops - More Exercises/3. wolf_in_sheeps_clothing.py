# animals = input().split(", ")
#
# current_animal = animals[-1]
#
# if current_animal == "wolf":
#     print("Please go away and stop eating my sheep")
# elif current_animal == "sheep":
#     sheep_counter = animals.count("sheep")
#     print(f"Oi! Sheep number {sheep_counter}! You are about to be eaten by a wolf!")


animals = input().split(", ")

wolf_index = animals.index('wolf') + 1

sheep_index = len(animals) - wolf_index

if wolf_index == len(animals):
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_index}! You are about to be eaten by a wolf!")
