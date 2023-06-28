import math

produced_biscuits = int(input())
number_of_workers = int(input())
other_factory_production = int(input())

total_biscuits = 0

for day in range(1, 30+1):
    biscuits_for_the_day = number_of_workers * produced_biscuits
    if day % 3 == 0:
        biscuits_for_the_day *= 0.75
    total_biscuits += math.floor(biscuits_for_the_day)

result = abs(total_biscuits - other_factory_production)
result_percentage = (result / other_factory_production) * 100

print(f"You have produced {total_biscuits} biscuits for the past month.")
if total_biscuits > other_factory_production:
    print(f"You produce {result_percentage:.2f} percent more biscuits.")
elif total_biscuits < other_factory_production:
    print(f"You produce {result_percentage:.2f} percent less biscuits.")
