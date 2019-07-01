name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# Here are some bonus ideas.

combat_level = 88
ranged_level = 94
mage_level = 94
strength_level = 87

print "Lifestring is a combat level %r with %r ranged, %r magic and %r strength." % (combat_level, ranged_level, mage_level, strength_level)

inch_to_cm = 2.54
kilos_to_pounds = 2.20462

print "754 Inches equals ", 754 * inch_to_cm, "Centimetres, and 200 Kilos equals ", kilos_to_pounds * 200, "pounds"
