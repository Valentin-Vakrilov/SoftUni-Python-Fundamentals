import re

string = input()

search_pattern = r"=([A-Z][A-Za-z]{2,})=|\/([A-Z][A-Za-z]{2,})\/"

matches = re.finditer(search_pattern, string)

destinations = []
travel_points = 0


for match in matches:
    current_match = match.group(0)
    destination = current_match[1:-1]
    destinations.append(destination)
    travel_points += len(destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
