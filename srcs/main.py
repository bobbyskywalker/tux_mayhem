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
import menu

# potential updates:
# TODO: enemies not colliding with each other would be nice
# TODO: enemies not spawning on tux
def game(game_settings, screen):
    # object setup
    bullets = Group()
    crosshair = sm.Cursor(screen)
    eq = Equipment(screen)
    hud = HUD(game_settings, screen, eq)
    tux = Tux(screen, hud, eq, game_settings)
    viruses = pygame.sprite.Group()
    skulls = pygame.sprite.Group()
    demons = pygame.sprite.Group()
    boss = Boss_foe(screen, tux, bullets, eq, game_settings)
    shop = Shop(screen, hud, eq, tux)

    # first init
    gf.update_screen(game_settings, screen, tux, bullets, crosshair, hud, eq, viruses, skulls, demons, boss)
    gf.print_wave_info(screen, hud)
    time.sleep(3)
    spawn_foes(viruses, skulls, demons, screen, tux, bullets, eq, hud, game_settings, boss)

    while 1:
        pygame.mouse.set_visible(False)    
        
        gf.update_screen(game_settings, screen, tux, bullets, crosshair, hud, eq, viruses, skulls, demons, boss)

        # new wave, shop available every two waves
        if not any(viruses) and not any(skulls) and not any(demons) and boss.alive == False:
            if hud.wave % 2 == 0 and hud.wave != 10:
                shop.active = True
                while (shop.active == True):
                    shop.buy_items()
            hud.wave += 1
            if hud.wave == 11:
                break
            gf.reset_tux_pos(tux)
            bullets.empty()
            gf.update_screen(game_settings, screen, tux, bullets, crosshair, hud, eq, viruses, skulls, demons, boss)
            gf.print_wave_info(screen, hud)
            time.sleep(3)
            spawn_foes(viruses, skulls, demons, screen, tux, bullets, eq, hud, game_settings, boss)

        angle = sm.get_angle_between((tux.rect.centerx, tux.rect.centery), crosshair.cursor_img_rect)
        gf.check_events(game_settings, screen, tux, bullets, angle, eq, viruses)        
        tux.update_pos()
        bullets.update()
        delete_bullets(bullets, hud)
        if eq.health <= 0:
            gf.game_over(screen)
            break
    gf.game_won(screen, hud)


def main():
    pygame.init()
    pygame.display.set_caption("TUX MAYHEM")
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    menu.menu_box(screen)
    game(game_settings, screen)
    pygame.quit()

main()