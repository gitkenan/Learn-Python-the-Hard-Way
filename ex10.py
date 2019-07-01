# We define a variable to be equal to a string, we contain a \t to 'tab' the line in. Hence why the string is 'I'm tabbed in'.
tabby_cat = "\tI'm tabbed in."
# We set this variable equal to a string which contains a new line command \n.
persian_cat = "I'm split\non a line"
# This is another variable set equal to a string, we cotain a sentence with the command \\, which is just printing the '\' symbol within a string,
#	by cancelling it out of the "" environment using the \ symbol. This is also how we can print the apostrophe ( ' ) or double quote ( " ) within a 
#	string "   ". Only single \s are printed"
blackslash_cat = "I'm \\ a \\ cat."
# A variable of a full paragraph, new line indents and very little effort in formatting. The environment is created with """ """.

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# We print all the variables we have set to see what happens.
print tabby_cat
print persian_cat
print blackslash_cat
print fat_cat 