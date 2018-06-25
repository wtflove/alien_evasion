import pygame

import sys

import random

from alien import Alien


def check_event(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def check_keydown_event(event, ship):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True


def check_keyup_event(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False


def update_screen(ai_settings, screen, ship, aliens):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def get_alien_x_range(ai_settings, alien):
    alien_x_range = ai_settings.screen_width - alien.rect.width

    return alien_x_range


def create_alien(screen, ai_settings, aliens):
    new_alien = Alien(screen, ai_settings)
    alien_x_range = round(get_alien_x_range(ai_settings, new_alien), 1)
    new_alien.rect.x = random.uniform(0, alien_x_range)
    new_alien.rect.bottom = 0
    aliens.add(new_alien)


def create_alien_fleet(screen, ai_settings, aliens):

    ai_settings.timer += 1
    if ai_settings.timer % ai_settings.alien_interval_factor == 0:
        create_alien(screen, ai_settings, aliens)


def update_aliens(screen, ai_settings, aliens):
    create_alien_fleet(screen, ai_settings, aliens)
    aliens.update()


# def print_numbers(ship):
#   print(str(ship.rect.centerx))
#   print(str(ship.moving_left))
#   print(str(ship.moving_right))
