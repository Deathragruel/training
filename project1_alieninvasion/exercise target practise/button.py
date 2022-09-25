import pygame

class Button:
	""" A class to render buttons with messages to the screen. """
	def __init__(self, tp_game, msg):
		self.screen = tp_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = tp_game.settings
		self.color = (128, 128, 128)
		self.width = 200
		self.height = 70
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.centery = self.screen_rect.centery
		self.rect.centerx = self.screen_rect.centerx - 50
		self.rect_center = (self.rect.center[0] - 30, self.rect.center[1] - 15)
		self.font = pygame.font.SysFont(None, 48)
		self.msg_color = (255, 255, 255)
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		""" A method to make the message and its font. """
		msg_str = str(msg)
		self.message = self.font.render(msg, True, self.msg_color, self.color)

	def draw_button(self):
		""" A method to draw the button to the screen. """
		pygame.draw.rect(self.screen, self.color, self.rect)
		self.screen.blit(self.message, self.rect_center)