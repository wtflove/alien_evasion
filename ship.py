import pygame


class Ship():
    def __init__(self, screen, ai_settings):
        self.ai_settings = ai_settings

        # get screen rect
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # place ship at center bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 20
        self.centerx_float = float(self.rect.centerx)

        # moving marks
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """update ship"""
        # move right & left
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx_float += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx_float -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.centerx_float
        # print(self.moving_right)

    def blitme(self):
        """draw ship on the screen"""
        self.screen.blit(self.image, self.rect)
