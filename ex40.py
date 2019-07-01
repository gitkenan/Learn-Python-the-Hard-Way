class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

	def song_len(self):
		print len(self.lyrics)

	def num_of_words(self):
		sentence_list = []
		for line in self.lyrics:
			split_line = line.split(" ")
			sentence_list.append(split_line)
		
		word_list = []
		for list in sentence_list:
			for word in list:
				word_list.append(word)
				
		print len(word_list)

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

rain_or_shine = Song(["Rain or shine",
						"We on that grind",
						"All my life",
						"On my life",
						"Til I close my eyes",
						"Rain or shine"])

in_the_zone = Song(["In the zone",
					"Alone at home I'm in the zone",
					"Silent is the mode on my phone",
					"When I'm in the zone"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

rain_or_shine.sing_me_a_song()

in_the_zone.sing_me_a_song()

print '-' * 10

seperate_lyrics = ["If you feel like you're being eaten",
			"From the inside mind stealing",
			"Children in a meeting",
			"Empty eyes confused "]

Song(seperate_lyrics).sing_me_a_song()

print '-' * 10

happy_bday.num_of_words()

bulls_on_parade.num_of_words()

rain_or_shine.num_of_words()