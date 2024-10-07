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
from shop import Shop
from enemies import *
import time

# TODO: automatic weapon
# TODO: enemies not colliding with each other would be nice
# TODO: ammo spawn fix lol
# TODO: enemies not spawning on tux
# TODO: score file savings
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
    viruses = pygame.sprite.Group()
    skulls = pygame.sprite.Group()
    demons = pygame.sprite.Group()
    shop = Shop(screen, hud, eq, tux)

    # first init
    gf.update_screen(game_settings, screen, tux, bullets, crosshair, hud, eq, viruses, skulls, demons)
    gf.print_wave_info(screen, hud)
    time.sleep(3)
    spawn_foes(viruses, skulls, demons, screen, tux, bullets, eq, hud, game_settings)

    while True:
        pygame.mouse.set_visible(False)    
        #check for events and update screen
        gf.update_screen(game_settings, screen, tux, bullets, crosshair, hud, eq, viruses, skulls, demons)

        # new wave
        if not any(viruses) and not any(skulls) and not any(demons):
            if hud.wave % 2 == 0:
                shop.active = True
                while(shop.active == True):
                    shop.buy_items()
            hud.wave += 1
            gf.reset_tux_pos(tux)
            gf.update_screen(game_settings, screen, tux, bullets, crosshair, hud, eq, viruses, skulls, demons)
            gf.print_wave_info(screen, hud)
            time.sleep(3)
            spawn_foes(viruses, skulls, demons, screen, tux, bullets, eq, hud, game_settings)

        angle = sm.get_angle_between((tux.rect.centerx, tux.rect.centery), crosshair.cursor_img_rect)
        gf.check_events(game_settings, screen, tux, bullets, angle, eq, viruses)        
        tux.update_pos()
        bullets.update()
        delete_bullets(bullets, hud)
        if eq.health <= 0:
            gf.game_over(screen)
            break      
run_game()