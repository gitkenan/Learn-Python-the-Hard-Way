from sys import argv

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file, 'r')
# indata = in_file.read()


out_file = open(to_file, 'w')
out_file.write(in_file.read())

print "Alright, all done."
