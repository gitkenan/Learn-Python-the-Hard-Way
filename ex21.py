def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b#

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b): 
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 10)
height = subtract(34, 4)
weight = multiply(30, 2)
IQ = divide(45, 15)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, IQ)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(IQ, 1))))

print "That becomes: ", what, "Can you do it by hand?"

print "Here is another puzzle."

here = add(subtract(24, 1023), divide(34, 100))

print "That becomes: ", here