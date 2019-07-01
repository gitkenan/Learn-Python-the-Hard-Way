ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') # split(' ', ten_things) - splits ten_things into a list of individual elements which were separated by ' '
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop() # pop(more_stuff) - brings forth the last element of the set, removes it from more_stuff and sets it equal to next_one
	print "Adding: ", next_one
	stuff.append(next_one) # append(next_one, stuff) - adds 'next_one' to the list of stuff
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop() # pop(stuff)
print ' '.join(stuff) # join(stuff, ' ')
print '#'.join(stuff[3:5]) # join(stuff[3:5], '#')
