import pygame
import time
import game_function as gf

from settings import Settings
from ship import Ship
# from alien import Alien
from pygame.sprite import Group


def run_game():
    """create & show screen"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Evasion")

    """create ship object"""
    ship = Ship(screen, ai_settings)

    """create alien object"""
    # alien = Alien(screen, ai_settings)

    """create a group of aliens"""
    aliens = Group()

    """program start time"""
    start_time = time.time()

    """set timer for aliens creation"""
    timer = 0

    while True:
        # timer += 1
        gf.check_event(ship)
        ship.update()
        gf.update_aliens(screen, ai_settings, aliens)
        # gf.print_numbers(ship)
        gf.update_screen(ai_settings, screen, ship, aliens)
        print(ai_settings.timer)


run_game()
