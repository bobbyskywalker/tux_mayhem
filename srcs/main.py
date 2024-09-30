import sys
import pygame
from settings import Settings
from tux import Tux
import game_functions as gf
from pygame.sprite import Group
import shooting_mechanics as sm
from bullet import delete_bullets
from HUD import HUD

#TODO: crosshair misses the bullet when shooting right, probable rect error

def run_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("tux mayhem")

    tux = Tux(screen)
    bullets = Group()
    crosshair = sm.Cursor(screen)
    hud = HUD(game_settings, screen)
    
    while True:
        pygame.mouse.set_visible(False)    
        #check for events and update screen
        
        gf.update_screen(game_settings, screen, tux, bullets, crosshair, hud)
        angle = sm.get_angle_between((tux.rect.centerx, tux.rect.centery), crosshair.cursor_img_rect)
        gf.check_events(game_settings, screen, tux, bullets, angle)        
        tux.update_pos()
        bullets.update()
        
        delete_bullets(bullets)
run_game()