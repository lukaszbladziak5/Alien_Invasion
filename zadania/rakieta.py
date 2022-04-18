import sys
import pygame

from gameSettings import GameSettings

class RocketGame():
	def __init__(self):

		self.gameSettings = GameSettings()
		self.rocket = Rocket()

		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.gameSettings.screen_width = self.screen.get_rect()
		self.gameSettings.screen_height = self.screen.get_rect()
		self.screen_color = self.gameSettings.bg_color

		pygame.display.set_caption("RocketGame")

	def run_game(self):

		while True:
			self._check_events()
			self.rocket.update()
			self._update_screen()