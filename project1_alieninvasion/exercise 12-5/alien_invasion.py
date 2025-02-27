import sys

import pygame

from settings import Settings
class AlienInvasion:
	""" Overall class to manage game assets and behaviour. """
	
	def __init__(self):
		""" Initialize the game, and create game resources. """
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")
	
	def run_game(self):
		""" Start the main loop for the game. """
		while True:
			self._check_events()
			self._update_screen()

	def _check_events(self):
		""" Respond to keypresses and mouse events. """
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					print(event.key)

	def _update_screen(self):
		""" Update images on the screen, and flip to the new screen. """
		self.screen.fill(self.settings.bg_color)
		pygame.display.flip()

# Make a game instance, and run the game.
if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()