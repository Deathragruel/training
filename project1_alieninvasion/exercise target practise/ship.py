import pygame

class Ship:
	""" A class to represent the ship that the player would control. """
	def __init__(self, tp_game):
		self.screen = tp_game.screen
		self.screen_rect = tp_game.screen.get_rect()
		self.settings = tp_game.settings
		self.image = pygame.image.load('ship.png').convert_alpha()
		self.rect = self.image.get_rect() 
		self.rect.midleft = self.screen_rect.midleft

		# Movement flags.
		self.moving_up = False
		self.moving_down = False
		self.moving_right = False
		self.moving_left = False

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		if self.moving_up and self.rect.y > 0:
			self.y -= self.settings.ship_speed

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		if self.moving_left and self.rect.x > 0:
			self.x -= self.settings.ship_speed

		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed

		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		self.screen.blit(self.image, self.rect)