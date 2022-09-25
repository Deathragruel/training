import pygame

class Settings:
	""" A class to store all the values which need to be initialized. """
	def __init__(self):
		self.flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
		self.color = (19, 24, 98)
		self.game_active = False

		# Ship settings.
		self.misses_allowed = 3

		# Bullet settings.
		self.bullet_width = 15
		self.bullet_height = 3
		self.bullet_color = (255, 255, 255)
		self.bullets_allowed = 3

	def initialize_dynamic_settings(self):
		self.ship_speed = 2.0
		self.bullet_speed = 1.5
		self.target_speed = 1.5

	def increase_speed(self):
		self.ship_speed *= 2
		self.bullet_speed *= 2
		self.target_speed *= 2