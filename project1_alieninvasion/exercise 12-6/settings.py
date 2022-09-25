class Settings:
	""" A class to store all settings for alien destruction. """
	def __init__(self):
		""" Initialize the game's static settings. """
		# Screen settings.
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (19, 24, 98)

		# Ship settings.
		self.ship_limit = 3

		# Bullet settings.
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (204, 28, 63)
		self.bullets_allowed = 3

		# Laser bullet settings.
		self.lb_width = 30
		self.lbs_allowed = 1

		# Alien settings.
		self.fleet_turn_speed = 10

		# How quickly the game speeds up.
		self.clicked = False
		self.speedup_scale = 1.1
		self.speeddown_scale = 1.1
		self.score_scale = 1.1
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		""" Initialize settings that change throughout the game. """
		self.ship_speed = 2 
		self.bullet_speed = 1.5
		self.lb_speed = 2
		self.alien_speed = 1.0
		# fleet direction of 1 represents down; -1 represents up.
		self.fleet_direction = 1
		# Scoring.
		self.alien_points = 50

	def increase_speed(self):
		""" Increase speed settings. """
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.lb_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points *= int(self.alien_points * self.score_scale)

	def easy_mode(self):
		""" Easy mode speed settings. """
		self.ship_speed *= (self.speedup_scale * 1.5)
		self.bullet_speed *= (self.speedup_scale * 1.5)
		self.lb_speed *= (self.speedup_scale * 1.5)
		self.alien_speed /= (self.speeddown_scale * 1.5)
		self.alien_points /= (self.speeddown_scale * 1.5)