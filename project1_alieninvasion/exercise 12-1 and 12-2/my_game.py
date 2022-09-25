import sys

import pygame

from settings import Settings

from character import Character

class MyGame:
	""" A class for the basic features of my game. """
	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((
			self.settings.window_width,
			self.settings.window_height,
			))
		pygame.display.set_caption("Alien Invasion")
		self.character = Character(self)

	def run_game(self):
		while True:
			self._check_events()
			self._update_screen()
	
	def _check_events(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.character.blitme()
		pygame.display.flip()

if __name__ == '__main__':
	mg = MyGame()
	mg.run_game()