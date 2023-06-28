def cars_received(cars_list, number):
    for car in range(number):
        current_car = input().split("|")
        car_model = current_car[0]
        mileage = int(current_car[1])
        fuel = int(current_car[2])

        cars_list[car_model] = {"mileage": mileage, "fuel": fuel}

    return cars_list


def car_commands(cars_list):

    while True:
        current_command = input().split(" : ")

        if current_command[0] == "Stop":
            break

        command_name = current_command[0]
        car_model = current_command[1]

        if command_name == "Drive":
            distance = int(current_command[2])
            fuel_consumed = int(current_command[3])

            if cars_list[car_model]["fuel"] >= fuel_consumed:
                cars_list[car_model]["mileage"] += distance
                cars_list[car_model]["fuel"] -= fuel_consumed
                print(f"{car_model} driven for {distance} kilometers. \
{fuel_consumed} liters of fuel consumed.")
            else:
                print("Not enough fuel to make that ride")

            if cars_list[car_model]["mileage"] >= 100000:
                print(f"Time to sell the {car_model}!")
                del cars_list[car_model]

        elif command_name == "Refuel":
            fuel_refueled = int(current_command[2])

            if cars_list[car_model]["fuel"] + fuel_refueled > 75:
                actual_fuel_refueled = 75 - cars_list[car_model]["fuel"]
                cars_list[car_model]["fuel"] = 75
                print(f"{car_model} refueled with {actual_fuel_refueled} liters")
            else:
                cars_list[car_model]["fuel"] += fuel_refueled
                print(f"{car_model} refueled with {fuel_refueled} liters")

        elif command_name == "Revert":
            kilometers = int(current_command[2])

            if cars_list[car_model]["mileage"] - kilometers < 10000:
                cars_list[car_model]["mileage"] = 10000
            else:
                cars_list[car_model]["mileage"] -= kilometers
                print(f"{car_model} mileage decreased by {kilometers} kilometers")

    return cars_list


def print_function(cars_list):
    for car_model in cars_list:
        mileage = cars_list[car_model]["mileage"]
        fuel = cars_list[car_model]["fuel"]
        print(f"{car_model} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")


def need_for_speed(number):
    cars_list = {}

    cars_received(cars_list, number)
    car_commands(cars_list)
    print_function(cars_list)


number_of_cars = int(input())
need_for_speed(number_of_cars)
