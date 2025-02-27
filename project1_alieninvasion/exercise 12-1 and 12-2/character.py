import pygame

class Character:
	""" This represents the main character for my game. """
	def __init__(self, game):
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()
		self.image = pygame.image.load("C:/images/character.bmp")
		self.rect = self.image.get_rect()
		self.rect.center = self.screen_rect.center

	def blitme(self):
		self.screen.blit(self.image, self.rect)