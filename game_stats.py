class GameStats:
	"""Monitorowanie danych statystycznych w grze "Inwazja obcych"."""

	def __init__(self, ai_game):
		"""Inicjazlizacja danych statystycznych."""

		self.settings = ai_game.settings
		self.reset_stats()

	def reset_stats(self):
		"""Inicjalizacja danych statystycznych, które mogą zmienić się 
		w trakcie gry."""

		self.ships_left = self.settings.ship_limit