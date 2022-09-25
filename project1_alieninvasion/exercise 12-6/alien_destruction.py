import sys
from time import sleep

import pygame

from random import randint

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star

class AlienDestruction:
	""" Overall class to manage game assets and behaviour. """
	def __init__(self):
		""" Initialize the game, and create game resources. """
		pygame.init()
		self.settings = Settings()
		flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
		# The laptop i am using as of now generates a 1366, 768 full screen.
		self.screen = pygame.display.set_mode((0, 0), flags)
		self.screen.set_alpha(None)
		self.screen_coordinates = pygame.display.get_window_size()
		self.screen_coordinate_x = self.screen_coordinates[0]
		self.screen_coordinate_y = self.screen_coordinates[1]
		# The second argument is the icontitle.
		pygame.display.set_caption("Alien Destruction", "Alien Destruction")
		
		# Create an instance to store game statistics and create a scoreboard.
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)
		
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.laser_bullets = pygame.sprite.Group()
		self.rain = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.stars = pygame.sprite.Group()
		self._create_star_grid()
		self._create_fleet()

		# Make the play button.
		self.play_button = Button(self, "Play")
		self.diff_1_button = Button(self, "Easy")
		self.diff_2_button = Button(self, "Normal")
		self.diff_3_button = Button(self, "Hard")

		# Music and sound settings.
		pygame.mixer.init()
		pygame.mixer.music.load('Autumn.ogg')
		self.bullet_sound = pygame.mixer.Sound('bullet_sound.ogg')
		self.bullet_sound.set_volume(0.3)
		self.alien_death_sound = pygame.mixer.Sound('alien_death_sound.ogg')
		self.alien_death_sound.set_volume(0.3)
		self.ship_hit_sound = pygame.mixer.Sound('ship_hit_sound.ogg')
		self.ship_hit_sound.set_volume(0.3)
		self.game_over_sound = pygame.mixer.Sound('game_over.ogg')
		self.game_over_sound.set_volume(0.3)
		pygame.mixer.music.play(loops=-1)

	def run_game(self):
		""" Start the main loop for the game. """
		while True:
			self._check_events()
			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()
			self._update_screen()

	def _check_events(self):
		""" Respond to keypresses and mouse events. """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				with open('save_high_score.txt', 'w') as file_object:
					file_object.write(str(self.stats.high_score))
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_play_button(self, mouse_pos):
		""" Start a new game when the player clicks Play. """
		self.button_clicked = (self.diff_1_button.rect.collidepoint(mouse_pos) or
			                   self.diff_2_button.rect.collidepoint(mouse_pos) or
			                   self.diff_3_button.rect.collidepoint(mouse_pos))
		play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if play_button_clicked or self.button_clicked and not self.stats.game_active:
			self._start_game(mouse_pos)

	def _check_keydown_events(self, event):
		""" Respond to keypresses. """
		
		if event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			with open('save_high_score.txt', 'w') as file_object:
				file_object.write(str(self.stats.high_score))
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_l:
			self._fire_laser_bullet()
		elif event.key == pygame.K_p:
			if not self.stats.game_active:
				self._start_game()

	def _start_game(self, mouse_pos):
		""" Start a new game. """
		if self.button_clicked:
			# Reset the game settings.
			self.settings.initialize_dynamic_settings()
			self._check_difficulty_buttons(mouse_pos)
			self.settings.clicked = True
		else:
			if not self.settings.clicked == True:
				# Reset the game settings.
				self.settings.initialize_dynamic_settings()
			# Reset the game statistics.
			self.stats.reset_stats()
			self.stats.game_active = True
			self.sb.prep_images()
			# Get rid of any remaining aliens or bullets.
			self.aliens.empty()
			self.bullets.empty()
			self.laser_bullets.empty()
			# Create a new fleet and center the ship.
			self._create_fleet()
			self.ship.center_ship()
			# Hide the mouse cursor.
			pygame.mouse.set_visible(False)
			# Music resume!
			pygame.mixer.music.unpause()

	def _check_difficulty_buttons(self, mouse_pos):
		""" Change difficulty. """
		game_active = self.stats.game_active
		if self.diff_1_button.rect.collidepoint(mouse_pos) and not game_active:
			self.settings.easy_mode()
		elif self.diff_2_button.rect.collidepoint(mouse_pos) and not game_active:
			pass
		elif self.diff_3_button.rect.collidepoint(mouse_pos) and not game_active:
			self.settings.increase_speed()
			self.settings.increase_speed()

	def _check_keyup_events(self, event):
		""" Respond to keypresses. """
		
		if event.key == pygame.K_DOWN:
			self.ship.moving_down = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		""" Create a new bullet and add it to the bullets group. """
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self, 'Normal')
			self.bullets.add(new_bullet)
			if self.stats.game_active:
				pygame.mixer.Sound.play(self.bullet_sound)

	def _fire_laser_bullet(self):
		""" Create a laser bullet and add it to the laser bullets group. """
		if len(self.laser_bullets) < self.settings.lbs_allowed:
			new_bullet = Bullet(self, 'Laser')
			self.laser_bullets.add(new_bullet)

	def _update_bullets(self):
		""" Update positions of bullets and get rid of old bullets. """
		self.bullets.update()
		self.laser_bullets.update()
		for bullet in self.bullets.copy():
			if bullet.rect.right >= self.screen_coordinate_x:
				self.bullets.remove(bullet)
		for bullet in self.laser_bullets.copy():
			if bullet.rect.right >= self.screen_coordinate_x:
				self.laser_bullets.remove(bullet)
		# Check for any bullets that have hit aliens.
		# If so, get rid of the bullet and the alien.
		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		""" Respond to bullet alien collisions. """
		# Remove any bullets and aliens that have collided.
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
		                                        True, True)
		special_collisions = pygame.sprite.groupcollide(self.laser_bullets,
			                                            self.aliens,
			                                            False, True)
		if collisions:
			for aliens in collisions.values():
				pygame.mixer.Sound.play(self.alien_death_sound)
				self.stats.score += self.settings.alien_points * len(aliens)
				self.sb.prep_score()
			self.sb.check_high_score()
		if special_collisions:
			for aliens in special_collisions.values():
				pygame.mixer.Sound.play(self.alien_death_sound)
				self.stats.score += self.settings.alien_points * len(aliens)
				self.sb.prep_score()
			self.sb.check_high_score()
		if not self.aliens:
			self._start_new_level()

	def _start_new_level(self):
		""" Draw existing bullets and create new fleet. """
		self.bullets.empty()
		self.laser_bullets.empty()
		self._create_fleet()
		self.settings.increase_speed()
		# Increase level.
		self.stats.level += 1
		self.sb.prep_level()		

	def _update_aliens(self):
		""" 
		Check if the fleet is at an edge,
		then update the position of all aliens in the fleet.
		"""
		self._check_fleet_edges()
		self.aliens.update()
		# Look for alien-ship collisions.
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()
		# Look for aliens hitting the left of the screen.
		self._check_aliens_reach_left()

	def _ship_hit(self):
		""" Respond to the ship being hit by an alien. """
		if self.stats.ships_left > 0:
			# Decrement ships_left and update scoreboard.
			self.stats.ships_left -= 1
			self.sb.prep_ships()
			# Get rid of any remaining  aliens and bullets.
			self.aliens.empty()
			self.bullets.empty()
			self.laser_bullets.empty()
			# Create a new fleet and center the ship.
			self._create_fleet()
			self.ship.center_ship()
			# Pause.
			sleep(0.5)
			pygame.mixer.Sound.play(self.ship_hit_sound)
		else:
			pygame.mixer.Sound.play(self.game_over_sound)
			self.stats.game_active = False
			pygame.mixer.music.pause()
			pygame.mouse.set_visible(True)

	def _check_aliens_reach_left(self):
		""" Check if any aliens have reached the left of the screen. """
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.left <= screen_rect.left:
				# Treat this the same as if the ship got hit.
				self._ship_hit()

	def _create_star_grid(self):
		""" Create stars in the background. """
		star_number = 0
		coordinate_x = int(((self.screen_coordinate_x/100) * 90))
		coordinate_y = int(((self.screen_coordinate_y/100) * 90))
		while star_number < 10:
			star = Star(self)
			self.stars.add(star)
			star_number += 1
		for star in self.stars:
			star.rect.x = randint(0, coordinate_x)
			star.rect.y = randint(0, coordinate_y)
			
	def _create_fleet(self):
		""" Create the fleet of aliens. """
		# Make an alien and find the number of aliens in a column.
		# Spacing between each alien is equal to one alien width.
		alien = Alien(self)
		alien_height = alien.rect.height
		alien_width = alien.rect.width
		available_space_y = self.screen_coordinate_y - (2 * alien_height)
		number_aliens_y =  available_space_y // (2 * alien_height)
		# Determine the number of columns of aliens that fit on the screen.
		ship_width = self.ship.rect.width
		available_space_x = (self.screen_coordinate_x 
		- (3 * alien_width) - ship_width)
		number_columns = available_space_x // (3 * alien_width)
		# Create the full fleet of aliens.
		for column_number in range(number_columns):
			for alien_number in range(number_aliens_y):
				self._create_alien(alien_number, column_number)

	def _create_alien(self, alien_number, column_number):
		""" Create an alien and place it in the column. """
		alien = Alien(self)
		alien_height = alien.rect.height
		alien_width = alien.rect.width
		alien.y = alien_height + (2 * alien_height * alien_number)
		alien.rect.y += alien.y
		alien.rect.x -= alien_width + (2 * alien_width * column_number)
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		""" Respond appropriately if any aliens have reached an edge. """
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		""" Turn the entire fleet and change it's direction. """
		for alien in self.aliens.sprites():
			alien.rect.x -= self.settings.fleet_turn_speed
		self.settings.fleet_direction *= -1

	def _update_screen(self):
		""" Update images on the screen, and flip to the new screen. """
		# Draw the play button if the game is inactive.
		if not self.stats.game_active:
			self.screen.fill((19, 24, 98))
			self.play_button.draw_button()
			self.diff_1_button.draw_button()
			self.diff_2_button.draw_button()
			self.diff_3_button.draw_button()
		else:
			self.screen.fill(self.settings.bg_color)
			self.stars.draw(self.screen)
			self.ship.blitme()
			for bullet in self.bullets.sprites():
				bullet.draw_bullet()
			for laser_bullet in self.laser_bullets.sprites():
				laser_bullet.draw_bullet()
			self.aliens.draw(self.screen)
			
		# Draw the score information.
		self.sb.show_score()
		pygame.display.flip()


if __name__ == '__main__':
	# Make a game instance, and run the game.
	ad = AlienDestruction()
	ad.run_game()