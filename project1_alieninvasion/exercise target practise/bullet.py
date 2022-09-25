import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	""" A class to represent a bullet shot by the ship. """
	def __init__(self, tp_game):
		super().__init__()
		self.screen = tp_game.screen
		self.settings = tp_game.settings
		self.ship = tp_game.ship
		self.color = self.settings.bullet_color
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
		                        self.settings.bullet_height)
		self.rect.midright = self.ship.rect.midright
		self.x = float(self.rect.x)

	def draw(self):
		""" Bring rect to the screen. """
		pygame.draw.rect(self.screen, self.color, self.rect)

	def update(self):
		""" Update bullet position. """
		self.x += self.settings.bullet_speed
		self.rect.x = self.x