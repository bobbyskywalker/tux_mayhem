import sys
import pygame
from settings import Settings
from tux import Tux
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()

    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("tux mayhem")

    tux = Tux(screen)
    bullets = Group()

    while True:
        
        #check for events and update screen
        gf.check_events(game_settings, screen, tux, bullets)        
        tux.update_pos()
        
        gf.update_screen(game_settings, screen, tux, bullets)
        bullets.update()

run_game()