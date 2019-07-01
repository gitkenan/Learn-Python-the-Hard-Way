tasks = {
	'1' : 'meditate',
	'2' : 'guitar',
	'3' : 'drink water',
	'4' : 'write',
	'5' : 'don\'t vape'
}

methods = {
	'meditate' : 'turn off screen',
	'guitar' : 'pick it up',
	'drink water' : 'pick up the water',
	'write' : 'meditate for a sec then notepad plus plus',
	'don\'t vape' : 'go out and do something else'
}

for x, y in methods.items():
	print "If you want to achieve your %s goal, just %s." % (x, y)