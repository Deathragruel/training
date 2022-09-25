import pygame

class Target:
	""" A class to represent a target to shoot as practise. """
	def __init__(self, tp_game):
		self.screen = tp_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = tp_game.settings
		self.image = pygame.image.load('target.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.topright = self.screen_rect.topright
		self.colliderect = pygame.Rect(0, 0, 100, 224)
		self.colliderect.center = self.rect.center
		self.y = float(self.rect.y)

		# Movement flags.
		self.moving_down = True
		self.moving_up = False

	def blitme(self):
		""" Draw target to the screen. """
		self.screen.blit(self.image, self.rect)

	def update(self):
		""" Update target's positions. """
		if self.rect.bottom >= self.screen_rect.bottom:
			self.moving_down = False
			self.moving_up = True

		if self.moving_up and self.rect.y > 0:
			self.y -= self.settings.target_speed

		if self.moving_down == False and self.rect.top == self.screen_rect.top:
			self.moving_up = False
			self.moving_down = True
		
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.target_speed

		self.rect.y = self.y
		self.colliderect.center = self.rect.center