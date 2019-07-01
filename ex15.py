# We import the argv package to be able to input the filename and script into the command line. The argv allows us to feed information into our script from the command line.
from sys import argv
# The two arguments we want to feed our script from the command line is the name of this script (ex15.py) and the name of our text file (ex15_sample.txt).
script, filename = argv










# We set the variable 'txt' to be equal to the 'open' function and feed it the filename, which the user is inputting into the command line. We will use this variable later in 
#	line 11.
txt = open(filename)
# We print a line which tells the user the name of the text file by using the %r (raw representation) method and inputting filename from the user's input in the command line.
print "Here's your file %r:" % filename
# We take the txt variable, which opens the given filename, and read it by adding .read() to the variable, and printing it. This line is quite densely packed so it's worth
# 	staring at it for a while. It's interesting that we still have to 'print' the text file after we have opened it and applied a read() function. This is because the read function
#	returns a string, and we must tell python what to do with this string. We of course would like to print the string. 
print txt.read() 
txt.close()








# This next line prints this next line.
print "Type the filename again:"
# Right, so we make a new variable and assign to it the promptation to the user which will look like '> ', clearly asking the user to pipe up and say some shit. This shit will be
# 	the name of the filename, again.
file_again = raw_input("> ")
# This next line simply opens the input of the user above which, if the user is submitting to their commanding overlord, should be the filename of the same file, again.
txt_again = open(file_again)
# We read the text_again variable above which opens the text file, and then print the string.
print txt_again.read()
txt_again.close()