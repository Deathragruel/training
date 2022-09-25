import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	""" A class to manage the ship. """
	def __init__(self, ad_game):
		""" Initialize the ship and set it's starting position. """
		super().__init__()
		self.screen = ad_game.screen
		self.settings = ad_game.settings
		self.screen_rect = ad_game.screen.get_rect()
		
		# Load the ship image and get it's rect.
		self.image = pygame.image.load('C:/Users/dell/Desktop/python_work/'
			                    'exercise 12-6/images/ship.png').convert_alpha()
		self.screen_coordinates = ad_game.screen_coordinates
		for coordinate in self.screen_coordinates:
			if coordinate == self.screen_coordinates[0]:
				new_coordinate_x = (coordinate/100) * 10
			else:
				new_coordinate_y = coordinate/2
		self.ship_position = (new_coordinate_x, new_coordinate_y)
		
		# Start each new ship around the midleft of the screen.
		self.rect = self.image.get_rect(midleft=self.ship_position)
		
		# Store decimal values for the ship's positions.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
		# Movement flag.
		self.moving_down = False
		self.moving_up = False
		self.moving_right = False
		self.moving_left = False

	def update(self):
		""" Update the ship's position based on the movement flags. """
		# Update the ship's x and y values, not the rect.
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed

		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed

		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed

		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		
		# Update rect object from self.x and self.y.
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		""" Draw the ship  at it's current location. """
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		""" Center the ship on the screen. """
		self.rect.midleft = self.ship_position
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)
