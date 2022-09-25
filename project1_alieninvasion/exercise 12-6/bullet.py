import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" A class to manage bullets fired from the ship. """

	def __init__(self, ad_game, bullet_type):
		""" Create a bullet object at the ship's current position. """
		super().__init__()
		self.screen = ad_game.screen
		self.settings = ad_game.settings
		self.color = self.settings.bullet_color
		self.type = bullet_type
		# Create a bullet rect at (0, 0) and then set correct position.
		if self.type == 'Normal':
			self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
			                    self.settings.bullet_height)
		else:
			self.rect = pygame.Rect(0, 0, self.settings.lb_width, 
				                    self.settings.bullet_height)
		self.rect.midright = ad_game.ship.rect.midright

		# Store the bullet's position as a decimal value.
		self.x = float(self.rect.x)

	def update(self):
		""" Move the bullet through the screen. """
		
		# Update the decimal position of the bullet.
		self.x += self.settings.lb_speed

		# Update the rect position.
		self.rect.x = self.x

	def draw_bullet(self):
		""" Draw the bullet to the screen. """
		if self.type == 'Normal':
			coloring = width=1
		else:
			coloring = width=0
		pygame.draw.rect(self.screen, self.color, self.rect, coloring)