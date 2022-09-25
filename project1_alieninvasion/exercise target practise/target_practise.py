import pygame

import sys

from settings import Settings
from ship import Ship
from bullet import Bullet
from target import Target
from game_stats import Gamestats
from button import Button

class TargetPractise:
	""" The main program for all methods to run the game. """
	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0, 0), self.settings.flags)
		self.screen_rect = self.screen.get_rect()
		pygame.display.set_caption("Target Practise")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.target = Target(self)
		self.stats = Gamestats(self)
		self.play_button = Button(self, "Play")

	def run_game(self):
		"""
		The main method that runs every other method from the classes infinitely.
		"""		 
		while True:
			self._check_events()
			if self.settings.game_active:
				self.ship.update()
				self.bullets.update()
				self.target.update()
				self._check_collisions()
			self._update_screen()

	def _check_events(self):
		""" Respond to keypresses and mouse inputs. """
		for event in pygame.event.get():

			if event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

			elif event.type == pygame.QUIT:
				sys.exit()

	def _check_play_button(self, mouse_pos):
		""" Respond to mouse clicking "Play" button. """
		play_button_rect = self.play_button.rect
		collision = play_button_rect.collidepoint(mouse_pos)
		game_active = self.settings.game_active
		if collision == True and game_active == False:
			self.stats.reset_stats()
			self.settings.initialize_dynamic_settings()
			pygame.mouse.set_visible(False)

	def _check_keydown_events(self, event):
		""" Respond to keypresses. """
		if event.key == pygame.K_q:
			sys.exit()

		elif event.key == pygame.K_UP:
			self.ship.moving_up = True

		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True

		elif event.key == pygame.K_RIGHT:
			self.ship.moving_right = True

		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True

		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		""" Respond to user removing finger from key. """
		if event.key == pygame.K_UP:
			self.ship.moving_up = False

		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

		elif event.key == pygame.K_RIGHT:
			self.ship.moving_right = False

		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		""" A method to add bullet to bullets group. """
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _draw_bullets(self):
		""" Draw bullets to the screen. """
		for bullet in self.bullets.sprites():
			bullet.draw()
			if bullet.rect.right > self.screen_rect.right:
				self.bullets.remove(bullet)
				self._respond_to_miss()

	def _check_collisions(self):
		""" Check if target and bullet have collided and respond if not. """
		collisions = []
		for bullet in self.bullets.sprites():
			pygame.bullet_rect = bullet.rect
			bullet_hit = pygame.bullet_rect.colliderect(self.target.colliderect)
			if bullet_hit:
				self.bullets.remove(bullet)
				collisions.append('True')
				if len(collisions) >= 5:
					collisions.clear()
					self.settings.increase_speed()

	def _respond_to_miss(self):
		""" Respond if the ship did not hit the target. """
		if self.settings.misses_allowed > 0:	
			self.settings.misses_allowed -= 1
			self.bullets.empty()
			pygame.time.wait(500)
		else:
			self.settings.game_active = False
			pygame.mouse.set_visible(True)

	def _update_screen(self):
		""" Updates all elements on the screen. """
		self.screen.fill(self.settings.color)
		if self.settings.game_active:
			self.ship.blitme()
			self._draw_bullets()
			self.target.blitme()
		else:
			self.play_button.draw_button()
		pygame.display.flip()

if __name__ == '__main__':
	""" Runs the program. (only if this is in the main program file.) """
	tp = TargetPractise()
	tp.run_game()