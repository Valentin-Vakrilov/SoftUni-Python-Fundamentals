number = float(input())

if number == 0:
    print("zero")
elif number > 0:
    if 1 < number < 1000000:
        print("positive")
    elif number < 1:
        print("small positive")
    elif number > 1000000:
        print("large positive")
else:
    if -1 > number > -1000000:
        print("negative")
    elif number > -1:
        print("small negative")
    elif number < -1000000:
        print("large negative")