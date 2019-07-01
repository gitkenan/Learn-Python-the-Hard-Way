cities = {
	'Manchester': 'MAN',
	'London': 'LON',
	'Paris': 'PAR',
	'Berlin': 'BER',
	'Merzig': 'MER',
}

areas = {
	'MAN': 'Midlands',
	'LON': 'South of England',
	'PAR': 'France',
	'BER': 'Germany',
	'MER': 'Switzerland',
}

cities['Belfast'] = 'BEL'
areas['BEL'] = 'Belfast'

print '-' * 10
print "Manchester is abbreviated as ", cities['Manchester']
print "London is abbreviated as ", cities['London']

print '-' * 10
print "Manchester is in the ", areas['MAN']
print "London is in the ", areas['LON']
print "Paris is in ", areas['PAR']

print '-' * 10
for abbrev, area in areas.items():
	print "%s is located in the area known as %s" % (abbrev, area)

print '-' * 10
print cities['Merzig']