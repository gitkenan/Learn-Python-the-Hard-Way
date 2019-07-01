# We assing a string to the variable x, containing the %d paramater to refer to a signed integer decimal 
x = "There are %d types of people." % 10
# Set the variable 'binary' as the string 'binary'
binary = "binary"
# Set the variable do_not as the string 'Don't'
do_not = "don't"
# Set the variable y to be equal to the following string, and we assign the %s's to be equal to binary and don't respectively. Notice there are 2 layers of embedding here.
y = "Those who know %s and those who %s." % (binary, do_not) #We put a strng inside a string here. Twice.

# We now print some sentences.
print x
# This sentence is already strung out.
print y 

# This uses the %r paramater which prints any python object using a repr() conversion.
print "I said: %r." % x #Here is a string inside a string.
# The %s paramater prints a string.
print "I also said: '%s'." % y # This is, in fact, a string within a string.
# It wasn't funny. I've heard it before.
hilarious = False 
# Let's take a closer look. Set this variable for later use.
joke_evaluation = "Isn't that joke so funny?! %r"
# We print the above and assign the %r paramater to the hilarious variable. 
print joke_evaluation % hilarious
# Let's set up some variables to print. First the west side, then the east side. Is da best.
w = "This is the left side of..."
e = "a string with a right side."
# Let's print the west side then the east side. This will make a longer string, as we are concatenating the two strings together by using the plus operation.
print w + e 