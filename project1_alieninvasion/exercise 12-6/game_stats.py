class GameStats:
	""" Track statistics for Alien Destruction. """
	def __init__(self, ad_game):
		""" Initialize statistics. """
		self.settings = ad_game.settings
		self.reset_stats()
		# Start Alien Destruction in an inactive state.
		self.game_active =  False
		# High score should never be reset.
		with open('save_high_score.txt') as file_object:
			self.high_score = float(file_object.read())

	def reset_stats(self):
		""" Initialize statistics that can change during the game. """
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1