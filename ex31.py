print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into a long dark tunnel."
	print "1. Walk forwards."
	print "2. Reach to your left."
	print "3. Reach to your right."
	
	insanity = raw_input("> ")
	
	if insanity == "1":
		print "You trip over a rock and a blade claims your organs! You bleed to death. Good job!"
	elif insanity == "2":
		print "You find a torch and press its button. A flame appears, revealing a few traps in the tunnel ahead."
		print "1. Walk forwards, walking around the knife on the floor."
		print "2. Walk forwards, jumping over the knife on the floor."
		print "3. Turn around, go into room 1 with the torch."
		
		walking = raw_input("> ")
		
		if walking == "1" or walking == "2":
			print "As you try your best to get past the knife, you activate a trip wire, which releases ten Grizzly bears to come running through the tunnel. They eat your limbs. Good job!"
		elif walking == "3":
			print "You enter room #1. The bear looks at you with cake on his face, stands up and roars in your direction, waiting for your next move."
			print "1. Throw the torch at the bear and leave the room. Come back for the cake."
			print "2. Walk towards the bear with eyes wide open."
			
			bear_time = raw_input("> ")
			
			if bear_time == "1":
				print "You hear the faint screams of a burning bear. You return into the room after a few minutes to find the cake unharmed. You eat it and die of dysentery. Good job!"
			elif bear_time == "2":
				print "The bear eats your head off. Good job!"
			else:
				print "This isn't an option. You die for being indecicive. Good job!"
		else:
			print "That isn't an option. A bear senses your pussy nature and eats your face off. Good job!"
	elif insanity == "3":
		print """You find a katana blade. A few bears run towards you, and you sharpen your blade on their
				arrival. You cut them up like a good watermelon. You throw the bears at the booby traps to
				move forward. You are able to get to the light at the end of the tunnel. Here, you find a 
				guitar and a beautiful woman. You marry the woman after a year and become a better guitarist.
				Eventually, you are shot to death in Crenshaw after becoming a rap legend and philanthropist.
				Good job!"""
	else:
		print "You aren't smart enough to do that yet. You die from AIDS. Good job!"
else:
	print "You stumble around and fall on a knife and die. Good job!"
	