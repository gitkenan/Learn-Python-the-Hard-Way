print "Let's practice everything."
# Note how we use the \ character to allow use of \ and ' within the '.' environment
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be fine: %s" % five
# This defines a function which performs simple maths and ultimately prints three seperate values.
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates


# The three values were set equal to the three variables 'beans', 'jars', 'crates'.
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
# %d pushes the decimal value. 
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
# At line 36, the value start_point changes to being ten times smaller.
start_point = start_point / 10

print "We can also do that this way:"
# This time, we assign three values to the %d's by just reading the function without brackets even! Amazing, but strange. 
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)