import sys
import pygame
from settings import Settings
from tux import Tux
import game_functions as gf
from pygame.sprite import Group
import shooting_mechanics as sm
from bullet import delete_bullets
from HUD import HUD
from equipment import Equipment
from enemies import *

# TODO: enemies not colliding with each other would be nice
# TODO: spawn enemies accordingly to the current wave
# TODO: after wave shop
# TODO: currency system
# TODO: scoreboard and score file savings
# TODO: weapon image and bullets firing from the weapon
# TODO: automatic weapon
# TODO: more enemies and more generic foe class, which is being inherited by other foes
# TODO: main menu
# TODO: wave 10 boss fight

def run_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("TUX MAYHEM")

    # object setup
    bullets = Group()
    crosshair = sm.Cursor(screen)
    eq = Equipment(screen)
    hud = HUD(game_settings, screen, eq)
    tux = Tux(screen, hud, eq, game_settings)

    # TODO: make them spawn accordingly to the current wave
    viruses = pygame.sprite.Group()
    spawn_foes(viruses, screen, tux, bullets, eq)
    
    while True:
        pygame.mouse.set_visible(False)    
        #check for events and update screen
        gf.update_screen(game_settings, screen, tux, bullets, crosshair, hud, eq, viruses)
        angle = sm.get_angle_between((tux.rect.centerx, tux.rect.centery), crosshair.cursor_img_rect)
        gf.check_events(game_settings, screen, tux, bullets, angle, eq, viruses)        
        tux.update_pos()
        bullets.update()
        delete_bullets(bullets)

        if eq.health <= 0:
            gf.game_over(screen)
            break      
run_game()