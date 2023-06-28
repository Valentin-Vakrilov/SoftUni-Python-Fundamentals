def loading_bar(some_number):
    if some_number == 100:
        return "100% Complete!" '\n' "[%%%%%%%%%%]"
    return f"{some_number}% [{'%' * (some_number // 10)}{'.' * (int(10 - (some_number / 10)))}]" '\n' "Still loading..."


number = int(input())
print(loading_bar(number))
