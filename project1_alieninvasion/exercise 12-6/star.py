import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	""" A class for a star background. """
	def __init__(self, ad_game):
		""" Initialize everything for the star. """
		super().__init__()
		self.screen = ad_game.screen
		self.image = pygame.image.load('C:/Users/dell/Desktop/python_work/'
			                    'exercise 12-6/images/star.png').convert_alpha()
		self.rect = self.image.get_rect()