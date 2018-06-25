import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, screen, ai_settings):
        """initialize alien"""
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings

        # initialize alien
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.x
        self.rect.y = self.screen_rect.y

        # float x & y of alien
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        # alien drop
        self.y += self.ai_settings.alien_speed_factor
        self.rect.y = self.y

    # def blitme(self):
    #     # show alien
    #     self.screen.blit(self.image, self.rect)
