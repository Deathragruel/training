""" Used as a module for users_2 """

class User:
	def __init__(self, first_name, last_name, username, location,
	             basic_description):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.location = location
		self.basic_description = basic_description
		self.login_attempts = 0
	def describe_user(self):
		print(f"Username: {self.username.lower()}")
		print(f"First name: {self.first_name.title()}")
		print(f"Last name: {self.last_name.title()}")
		print(f"Location: {self.location.title()}")
		print(f"Description: {self.basic_description}")
	def greet_user(self):
		print(f"Hello, {self.username.lower()}. Thank you for logging in again!")
	def increment_login_attempts(self, add_login_attempt):
		if add_login_attempt < 0:
			print("You can't 'add' when your using negative numbers. That makes"
				" no sense!")
		else:
			self.login_attempts += add_login_attempt
	def reset_login_attempts(self):
		self.login_attempts = 0