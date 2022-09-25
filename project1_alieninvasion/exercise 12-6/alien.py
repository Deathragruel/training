import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	""" A class to represent a single alien in the fleet. """
	def __init__(self, ad_game):
		""" Initialize the alien and set it's starting position. """
		super().__init__()
		self.screen = ad_game.screen
		self.settings = ad_game.settings
		self.coordinate_x = float((ad_game.screen_coordinate_x/100) * 92.5)
		self.coordinate_y = float((ad_game.screen_coordinate_y/100) * 2.5)
		# Load the alien image and set it's rect attribute.
		self.image = pygame.image.load('C:/Users/dell/Desktop/python_work/'
			                   'exercise 12-6/images/alien.png').convert_alpha()
		self.rect = self.image.get_rect()
		# Start each new alien near the top right of the screen.
		self.rect.x = self.coordinate_x
		self.rect.y = self.coordinate_y
		# Store the alien's exact position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def check_edges(self):
		""" Return True if an alien is at the edge of the screen. """
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
			return True

	def update(self):
		""" Move the aliens down or up. """
		self.y += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.y = self.y