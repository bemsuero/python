# assigning cars
cars = 100
# assigning carseats
space_in_a_car = 4.0
# assigning drivers
drivers = 30
# assigning passengers
passengers = 90
# assigning empty cars
cars_not_driven = cars - drivers
# assigning driven cars
cars_driven = drivers
# assigning amount of space available
carpool_capacity = cars_driven * space_in_a_car
# assigning amount of passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")
