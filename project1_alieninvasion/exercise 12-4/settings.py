class Settings:
	""" A class to store all settings for Rocket Game. """
	""" Initialize the game's settings. """
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (255, 255, 255)

		# Ship settings
		self.rocket_speed = 1.5