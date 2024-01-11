import sys
import pygame
from settings import Settings
from ship import Ship
import game_fucts as gf
from pygame.sprite import Group
from alien import Alien
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Aliaen invasion")
    # Make a ship.
    ship = Ship(screen,ai_settings)
    # Make a group to store bullets in.
    bullets = Group()
    # Make an alien.
    alien = Alien(ai_settings, screen)
    aliens = Group()
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen,ship, aliens)

    while True:
        #Watch for keyboard and mouse events.
        gf.check_event(ai_settings,screen,ship,bullets)
        ship.upd()
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)
       
run_game()