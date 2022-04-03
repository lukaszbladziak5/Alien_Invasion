import pygame

class Bird():

	def __init__(self, b_game):
		self.screen = b_game.screen
		self.screen_rect = b_game.screen.get_rect()

		self.image = pygame.image.load('images/bird_small.bmp')
		self.rect = self.image.get_rect()

		self.rect.center = self.screen_rect.center

	def blit_bird(self):
		self.screen.blit(self.image, self.rect)
