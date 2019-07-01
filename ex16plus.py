print "Type the filename you would like to open and read:"
file = raw_input("> ")
text = open(file, 'r')
print text.read()
text.close()