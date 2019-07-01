from sys import exit

def runescape():
	print "You turn around and turn on the computer."
	print "Suddenly you see yourself in Gillenor by the Grand Exchange with 10,000 alchables."
	print "Would you like to alch an item?"
	exp = 140000
	alch_choice = raw_input("> ")
	
	if alch_choice == "yes":
		exp = exp + 65
		print "Your Magic experience is now", exp
		alch_again = "yes"
		while exp < 150000 and alch_again == "yes":
			print "Would you like to alch again?"
			realch()

def realch():
	alch_again = raw_input("> ")
		if alch_again == "yes":
			exp = exp + 65
			print "Your Magic experience is now", exp
		else:
			dead("You don't want to make gains. You stand at the GE until you die of hunger.")
	
def gold_room():
	print "This room is full of gold. How much will you take?"
	
	next = raw_input("> ")
	how_much = int(next)
	if how_much > 50:
		dead("Woah, okay, you take the gold you greedy person!")
	else:
		dead("Man, learn to type a number.")
	
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")


def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		next = raw_input("> ")
		
		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."


def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else: 
		cthulhu_room()


def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left and a computer behind you."
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	elif next == "use computer":
		runescape()
	else:
		dead("You stumble around the room until you starve.")


start()

