# we import argv module from sys package
from sys import argv
# argv lets us input files and scripts from the command line under python
script, input_file = argv
# we defin a function which prints the whole file 'f' after reading it. 'f' is the input file. this function is called print_all
def print_all(f):
	print f.read()
# we define a function 'rewind' to brings the file's current position back to the start, which is the offset = 0. yes, we have to bring the file back to the start if we want to read it again.
def rewind(f):
# the seek function is applied to f, which changes the current 'tape position' of the file to the offset, which in this case is 0 (again, why did i explain this twice?)
	f.seek(0)
# we define the 'print_a_line' function to, surprise surprise, print the line count and read a particular line of 'f', which is the input file.
def print_a_line(line_count, f):
	print line_count, ":", f.readline()
# we set the variable 'current_file' to be equal to the opened input file. we do this by setting it equal to the value of putting 'input_file' into open().
current_file = open(input_file)
# we talk to the user.
print "First let's print the whole file:\n"
# we use the function on line 6 to print an open function which is being 'read'. this is the whole file.
print_all(current_file)
# reload time that finna last text file was HARD. 
print "Now let's rewind, kind of like a tape."
# this function brings it back like we described in line 8 forwards, using the seek function.
rewind(current_file)
# we talk to the user
print "Let's print three lines:"
#in line 28 and 29, the current_line is actually equal to 1. 
current_line = 1
print_a_line(current_line, current_file)
# now we change the current line number to 2, which is true for lines 31 and 32. this is fascinating, so the variable changes just like the lines of text have to be 'rolled-back' in the
# code. it's like we're operating in a tape reel.
current_line += 1
print_a_line(current_line, current_file)
# line 3 will be printed. remember, these are both runnings = callings = usings of the function
current_line += 1
print_a_line(current_line, current_file)
