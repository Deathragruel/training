import pygame.font

class Button:
	def __init__(self, ad_game, msg):
		""" Initialize button attributes. """
		self.response = msg
		self.screen = ad_game.screen
		self.screen_rect = self.screen.get_rect()
		self.screen_coordinate_x = ad_game.screen_coordinate_x
		self.screen_coordinate_y = ad_game.screen_coordinate_y
		# Set the dimensions and property of the button.
		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48, italic=True)
		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		# The button message needs to be prepped only once.
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		""" Turn msg into a rendered image and center text on the button. """
		# Although self.button_color is completely unnecessary to add as an
		# argument, it results in an increase in performance.
		if self.response == "Play":
			self.rect.center = self.screen_rect.center
		self._display_difficulty_levels()
		self.msg_image = self.font.render(msg, True, self.text_color,
			                              self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		# Draw blank button and then draw message.
		if self.response == "Play":
			self.rect.center = self.screen_rect.center
		self._display_difficulty_levels()
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

	def _display_difficulty_levels(self):
		""" If statements for displaying difficulty level buttons. """
		self.rect_x = float(self.screen_rect.centerx - (0.0732 * self.screen_coordinate_x))
		if self.response == "Normal":
			self.rect.x = self.rect_x
			self.rect.y = ((self.screen_rect.centery/100) * 120)
		elif self.response == "Easy":
			self.rect.x = float(self.rect_x - 300)
			self.rect.y = ((self.screen_rect.centery/100) * 120)
		elif self.response == "Hard":
			self.rect.x = float(self.rect_x + 300)
			self.rect.y = ((self.screen_rect.centery/100) * 120)