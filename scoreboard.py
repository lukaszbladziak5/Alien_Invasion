import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
	"""Klasa przeznacznoa do przedstawiania informacji o punktacji."""

	def __init__(self, ai_game):
		"""Inicjalizacja atrybutów dotyczących pumktacji."""

		self.ai_game = ai_game
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats

		# Ustawienia czcionki dla informacji o punktacji.
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		# Przygotowanie początkowych obrazów z punktacją.
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		"""Przekształcenie punktacji na wygenerowany obraz."""

		rounded_score = round(self.stats.score, -1)
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True,
			self.text_color, self.settings.bg_color)

		# Wyświetlenie punktacji w prawym górnym rogu ekranu.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_high_score(self):
		"""Konwersja najlepszego wyniku w grze na wygenerowany obraz."""

		high_score = round(self.stats.high_score, -1)
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
			self.text_color, self.settings.bg_color)

		# Wyświetlenie najlepszego wyniku na środku ekranu, przy górnej
		# krawędzi.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		"""Przekształcenie numeru poziomu na wygenerowany obraz."""

		level_str = "Level " + str(self.stats.level)
		self.level_image = self.font.render(level_str, True,
			self.text_color, self.settings.bg_color)

		# Wyświetlenie numeru poziomu pod aktualną punktacją.
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		"""Wyświetla liczbę staków, jakie pozostały graczowi."""

		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_game)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)

	def show_score(self):
		"""Wyświetlenie punktacji, poziomu i liczby statków na ekranie."""

		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)

	def check_high_score(self):
		"""Sprawdzenie, czy mamy nowy najlepszy wynik osiągnięty dotąd
		w grze."""

		if self.stats.score >= self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.prep_high_score()