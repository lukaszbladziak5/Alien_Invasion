class GameStats:
	"""Monitorowanie danych statystycznych w grze "Inwazja obcych"."""

	def __init__(self, ai_game):
		"""Inicjazlizacja danych statystycznych."""

		self.settings = ai_game.settings
		self.reset_stats()

		# Najlepszy wynik nigdy nie powinien zostać wyzerowany.
		self.high_score = 0

		# Uruchomienie gry "Inwazja obcych" w stanie nieaktywnym.
		self.game_active = False

	def reset_stats(self):
		"""Inicjalizacja danych statystycznych, które mogą zmienić się 
		w trakcie gry."""

		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1