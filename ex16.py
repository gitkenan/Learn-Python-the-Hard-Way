# Please import argv, I need you argv.
from sys import argv
# In the command line we write ex16.py and the name of the text file we wish to write over.
script, filename = argv
# Some simple instructions. The user is then prompted to either continue by pressing enter, or to cancel the whole operation altogether by doing CTRL-C.
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# This prompts the user with a question mark.
raw_input("?")
# We now tell the user we will open the file. We then continue by opening the given filename, and we give the open('filename', 'mode') the mode = 'w' which is used for writing
#	over a file. 
print "Opening the file..."
# We set the variable 'target' equal to the open action on the given filename. This sets 'target' equal to the open file, ready to write over.
target = open(filename, 'w')
# Time to empty the file 'target' which is the filename.
print "Truncating the file. Goodbye!"
target.truncate()
# These are some raw inputs for the user to overwrite the file with.
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
# Okay. This is what we need to tidy up. We are applying the 'write()' function to the target file here. 
print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()