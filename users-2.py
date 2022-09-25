class Privileges:
	def __init__(self, privileges =  ['can add post', 'can delete post',
	                                  'can ban post']):
		self.privileges = privileges
	def show_privileges(self):
		print(self.privileges)

class Admin(User):
	def __init__(self, first_name, last_name, username, location,
		         basic_description):
		super().__init__(first_name, last_name, username, location, 
		             basic_description)
		self.privileges = Privileges()