from random import randint

class Die:
	""" A simple attempt to model throwing a dice or die."""
	def __init__(self, sides = 6):
		self.sides = sides
	def roll_die(self):
		print(randint(1, self.sides))
	def incrementing_or_decrementing_roll_die(self, modification):
		result = randint(1, self.sides)
		print(result + modification)
	def multiplying_roll_die(self, modification_2):
		result_2 = randint(1, self.sides)
		print(result_2 * modification_2)
	def divisible_roll_die(self, modification_3):
		result_3 = randint(1, self.sides)
		print(result_3/modification_3)

print("d6:")
throwing_dice = Die()
throwing_dice.roll_die()

print("\nd10:")
throwing_dice = Die(10)
throwing_dice.roll_die()

print("\nd20:")

throwing_dice = Die(20)
throwing_dice.roll_die()

print("\ndice(plus or minus-able version):")

throwing_dice = Die()
throwing_dice.incrementing_or_decrementing_roll_die(42)

print("\ndice(multiplying version):")

throwing_dice = Die()
throwing_dice.multiplying_roll_die(1)

print("\ndice(divisible version):")

throwing_dice = Die()
throwing_dice.divisible_roll_die(1)