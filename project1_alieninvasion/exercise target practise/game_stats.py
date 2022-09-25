class Gamestats:
	""" 
	A class to store when the game will be running,
	and what could cause it to not run.
	"""
	def __init__(self, tp_game):
		""" Initialize the properties required. """
		self.settings = tp_game.settings

	def reset_stats(self):
		""" 
		It allows for properties to be changed while the program is running.
		"""
		self.settings.game_active = True
		self.settings.misses_allowed = 3