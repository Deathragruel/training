""" Used as a module for my_restaurant. """

class Restaurant:
	""" A simple model for a restaurant """
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	def describe_restaurant(self):
		print(f"Whenever we go to a restaurant,"
		 f" we mostly go to {self.restaurant_name.title()}.")
		print(f"It's specialty is a serving of {self.cuisine_type}.")
	def open_restaurant(self):
		print(f"Right now, {self.restaurant_name.title()} is open!")
	def set_number_served(self, served_number):
		if served_number >= self.number_served:
			self.number_served = served_number
		else:
			print("You can't reduce the number you served.")
	def increment_number_served(self, serve_number):
		if serve_number < 0:
			print("You can't decrease the amount you served.")
		else:
			self.number_served += serve_number

class IceCreamStand(Restaurant):
	""" A simple attempt to model an ice cream stand (form of restaurant) """
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavours = ['blueberry', 'strawberry', 'chocokate', 'mango']
	def display_ice_cream_flavours(self):
		print(f"The following is a list of {self.restaurant_name}'s available flavours:")
		print(self.flavours)