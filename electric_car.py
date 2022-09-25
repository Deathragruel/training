# A module importing a module that is used by my_electric_car.py and such files.
from car import Car

class Battery:
	""" A simple attempt to model a battery for an electric car. """
	def __init__(self, battery_size=75):
		""" Initialize the battery's attributes. """
		self.battery_size = battery_size
	def describe_battery(self):
		""" Print a statement describing the battery size. """
		print(f"This electric car has a {self.battery_size}-kWh battery.")
	def get_range(self):
		""" Print a statement about the range this battery provides. """
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge.")
	def upgrade_battery(self):
		if self.battery_size != 100:
			self.battery_size = 100
			print("Your battery has been upgraded!")

class ElectricCar(Car):
	""" Represent aspects of a car, specific to electric vehicles. """
	def __init__(self, manufacturer, model, year):
		""" Initialize attributes of the parent class.
		    Then initialize attributes specific to an electric car. """
		super().__init__(manufacturer, model, year)
		self.battery = Battery()
	def fill_gas_tank(self):
		""" Example of overriding a parent class method """
		print("This car does not need a gas tank!")