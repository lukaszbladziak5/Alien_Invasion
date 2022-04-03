import sys
import pygame

from sett import Settings
from bird import Bird

class Blue_Bird():
	def __init__(self):
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width,
			self.settings.screen_height))
		pygame.display.set_caption("Blue_Bird")
		self.bird = Bird(self)
		self.bg_color = self.settings.bg_color

	def run_game(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			self.screen.fill(self.bg_color)
			self.bird.blit_bird()

			pygame.display.flip()

if __name__ == '__main__':
	b = Blue_Bird()
	b.run_game()