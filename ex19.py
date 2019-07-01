# This defines the function we will use throughout the whole script.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count # This leaves the cheese_count to be inserted later.
	print "You have %d boxes of crackers!" % boxes_of_crackers # This does the same as the above line but with a different variable.
	print "Man that's enough for a party!"
	print "Get a blanket.\n" # This \n creates a new line to separate the instances of the function to make our command output to look clean.


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) # Running the function with number values


print "OR, we can use variables from our script:"
amount_of_cheese = 10 # Setting variables 
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # Calling the function with the variables we set


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) # Using the function with math as values


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # Calling the function with math and variables.