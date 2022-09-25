from users_2 import *

user_0 = User('albert', 'einstein', 'aeinstein', 'princeton',
	          'I created the formula for the atomic bomb!')
user_1 = User('marie', 'curie', 'mcurie', 'warsaw, poland',
	          'I discovered radium and polonium!')
user_2 = User('isaac', 'newton', 'inewton', 'england',
	          'I made the three laws of motion!')
user_3 = User('nikola', 'tesla', 'ntesla', 'new york',
	          'I enlightened the world!')

user_0.describe_user()
user_0.greet_user()
print("\n")

user_1.describe_user()
user_1.greet_user()
print("\n")

user_2.describe_user()
user_2.greet_user()
print("\n")

user_3.describe_user()
user_3.greet_user()
print("\n")

user = User('Joey', 'Rebecca', 'Jyabecca', 'Moon',
	        'I destroy planets :):):)')
user.describe_user()
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
user.increment_login_attempts(1)
print(f"User login attempts (thus far): {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts (after reset): {user.login_attempts}\n")

admin = Admin('Barber', 'Retta', 'Barbaretta', 'Mars',
	          'I am admin.')
admin.privileges.show_privileges()