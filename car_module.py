""" A class that can be used to represent a car (usable as module for car.py) """
class Car:
	""" A simple attempt to represent a car """
	def __init__(self, manufacturer, model, year):
		""" Initialize attributes to describe a car """
		self.manufacturer = manufacturer
		self.model = model
		self.year = year
		self.odometer_reading = 0
	def get_descriptive_name(self):
		""" Return a neatly formatted descriptive name. """
		long_name = f"{self.year} {self.manufacturer} {self.model}"
		return long_name.title()
	def read_odometer(self):
		""" Print a statement about the car's mileage """
		print(f"This car has {self.odometer_reading} miles on it.")
	def update_odometer(self, mileage):
		""" Set the odometer reading to the given value.
		    Reject the change if it attempts to roll the odometer back """
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def increment_odometer(self, miles):
		""" Add the given amount to the odometer reading. """
		if miles < 0:
			print("Negative increments are rejected.")
		else:
			self.odometer_reading += miles