# This variable is given the value of the following string.
days = "Mon Tue Wed Thu Fri Sat Sun"
# This variable is a string which starts on new lines using \n to create new lines.
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# This prints a string followed by another string which we have already preset to the 'days' variable.
print "Here are the days: ", days
# Since we are printing two seperate strings, we add a comma between them.
print "Here are the months: ", months
# Here we print three quotation marks and follow it up with a whole paragraph of information. This means that we get to not worry about line breaks
#	and python will do most of the formatting for us. What a lovely little trick. 
print """
There's something going on here.
With the three double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
