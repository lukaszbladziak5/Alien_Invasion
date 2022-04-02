import sys
import pygame

class AlienInvasion:
	"""Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania
	gry."""

	def __init__(self):
		"""Inicjalizacja gry i utworzenie jej zasobów."""
		
		pygame.init()

		#Zdefiniowanie powierzchni (okna) do gry i nadanie jej tytułu.
		self.screen = pygame.display.set_mode((1200, 800))
		pygame.display.set_caption("Inwazja Obcych!")

		#Zdefiniowanie koloru tła.
		self.bg_color = (230, 230, 230)

	def run_game(self):
		"""Rozpoczęcie pętli głównej gry."""
		
		while True:
			#Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			#Odświeżenie ekranu w trakcie każdej iteracji pętli.
			self.screen.fill(self.bg_color)

			#Wyświetlenie ostatnio zmodyfikowanego ekranu.
			pygame.display.flip()

if __name__ == '__main__':
	#Utworzenie egzemplarza gry i jej uruchomienie.
	ai = AlienInvasion()
	ai.run_game()