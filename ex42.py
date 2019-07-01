## Animal is-a object
class Animal(object):
	
	def __init__(self, colour):
		## animal has-a colour
		self.colour = colour

	def tell_us(self, colour):
		print colour
## Dog is-a animal
class Dog(Animal):

	def __init__(self, name):
		## dog has-a name
		self.name = name

	def saywoof(self, name):
		print "Woof, says", name

## Cat is-a animal
class Cat(Animal):

	def __init__(self, name):
		## cat has-a name
		self.name = name

## Person is-a object
class Person(object):
	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## hmm... s__init__till haven't worked out this strange magic
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a fish
class Salmon(Fish):
	pass

## Halibut is-a fish
class Halibut(Fish):
	pass

## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## Mary is-a personn
mary = Person("Mary")

## mary has-a pet named 'satan'
mary.pet = satan

## Frank is-a employee and has-a name 'Frank' and salary 1200000
frank = Employee("Frank", 1200000)

## Frank has-a pet which is-a rover
frank.pet = rover

## Flipper is an instance of the Fish class
Flipper = Fish()

## Crouse is an instance of the fish class
Crouse = Fish()

## Harry is an instance of the Halibut class
Harry = Halibut()

Animal.tell_us(Animal("Gold"), "purple")

Dog.saywoof(Dog("Love"), "Lobby")

