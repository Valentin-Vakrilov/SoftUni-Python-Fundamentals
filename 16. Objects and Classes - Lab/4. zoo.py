class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)} \nTotal animals: {Zoo.__animals}"
        elif species == "fish":
            return f"Fish in {self.name}: {', '.join(self.fish)} \nTotal animals: {Zoo.__animals}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)} \nTotal animals: {Zoo.__animals}"


zoo = Zoo(input())

counter = int(input())

for row in range(counter):
    current_row = input().split()
    species = current_row[0]
    name = current_row[1]
    zoo.add_animal(species, name)

specie = input()

print(zoo.get_info(specie))


# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == "mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "bird":
#             self.birds.append(name)
#
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ""
#         if species == "mammal":
#             result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
#         elif species == "fish":
#             result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
#         elif species == "bird":
#             result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
#
#         result += f"Total animals: {Zoo.__animals}"
#         return result
#
# zoo_name = input()
# zoo = Zoo(zoo_name)
# count = int(input())
#
# for i in range(count):
#     animal = input().split(" ")
#     species = animal[0]
#     name = animal[1]
#     zoo.add_animal(species, name)
#
# info = input()
# print(zoo.get_info(info))
