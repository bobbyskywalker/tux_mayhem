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
from enemies import Virus_foe

#TODO: enemies and health mechanics
# new weapon

def run_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("TUX MAYHEM")

    bullets = Group()
    crosshair = sm.Cursor(screen)
    eq = Equipment(screen)
    hud = HUD(game_settings, screen, eq)
    tux = Tux(screen, hud, eq, game_settings)
    enemies = Virus_foe(screen, tux)
    

    while True:
        pygame.mouse.set_visible(False)    
        #check for events and update screen
        gf.update_screen(game_settings, screen, tux, bullets, crosshair, hud, eq, enemies)
        angle = sm.get_angle_between((tux.rect.centerx, tux.rect.centery), crosshair.cursor_img_rect)
        gf.check_events(game_settings, screen, tux, bullets, angle, eq)        
        tux.update_pos()
        bullets.update()
        
        delete_bullets(bullets)
run_game()