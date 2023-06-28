class Party:
    def __init__(self):
        self.people = []


people_at_the_party = Party()

command = input()

while command != "End":
    people_at_the_party.people.append(command)
    command = input()

print(f"Going: {', '.join(people_at_the_party.people)}")
print(f"Total: {len(people_at_the_party.people)}")
