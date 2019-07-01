# There are 100 cars.
cars = 100
# We name this variable as being equal to 4.
space_in_a_car = 4
# We have 30 drivers.
drivers = 30
# The variable 'passengers' is given the value 90.
passengers = 90
# The cars which aren't driven are given by the following, since there is only one of each driver.
cars_not_driven = cars - drivers
# Each driver drives their own car. They're doing their job, what do you expect?
cars_driven = drivers
# The amount we can fit is given by the number of cars multiplied by the amount each car holds.
carpool_capacity = cars_driven * space_in_a_car
# Average equals total passengers divided by number of cars.
average_passengers_per_car = passengers / cars_driven
# We use the cars variable instead of displaying 100.
print "There are", cars, "cars available."
# We continue to use preset variables and print some text.
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Here are some extras

print "Here are some bonus mathematical calculations for you."
i = 420.0
j = 17.0
k = 9.20

print "We know that i + j + k =", i + j + k
print "Furthermore, i x j =", i*j 
print "Also, i / j =", i/j 
print "We also know that i * j + k / j =", i*j + k/j 
print "Hey %s there." % "you."
 