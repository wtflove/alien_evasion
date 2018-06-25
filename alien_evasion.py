import pygame
import game_function as gf
from settings import Settings
from ship import Ship

def run_game():
    """create & show screen"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Evasion")

    """create ship object"""
    ship = Ship(screen, ai_settings)
    while True:
        gf.check_event(ship)
        ship.update()
        # gf.print_numbers(ship)
        gf.update_screen(ai_settings, screen, ship)



run_game()


