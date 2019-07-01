# This variable sets up the possibility of printing four consecutive things. Let's try!
formatter = "%r %r %r %r"

# First let's replace each instance of %r by some natural numbers.
print formatter % (1, 2, 3, 4)
# Now let's do the same but with words.
print formatter % ("one", "two", "three", "four")
# Something something boolean operators.
print formatter % (True, False, False, True)
# This changed %r from being a function in 'formatter' to being normal strings of letters. It prints '%r %r %r %r' four times.
print formatter % (formatter, formatter, formatter, formatter)
# These are all printed on the same line with single apostrophe quotation marks, other than in the third sentence because it contains an apostrophe,
	# so to avoid confusion it will print this line with double quotation marks.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."

# Some bonus freestyle ideas from this, as I think it is an interesting use of the %r paramater. 

fibonacci = "%r is the first prime, %r is the second prime, %r is the fourth prime and %r is the third prime." 

print fibonacci % (2, 3, 7, 5)
