# We assign some variables.
people = 20
cars = 30
buses = 40

# One of the indented lines will be executed, depending on the Boolean values of the statments after 'if' and 'elif'.
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

# Same goes here.
if buses > cars:
	print "That's too many buses."
# The 'elif' is saying IF WE SKIPPED THE ABOVE because it's not true, then is buses < cars? If it is, run the code under elif and forget the else. If not, then see 'else' and run the code under that.
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, lets just take the buses."
else:
	print "Fine, let's stay home then."
# We do the same but we use a more complicated Boolean variable statememnt. 
if people > cars or buses > cars:
	print "Either we got enough cars or we should take the bus."
