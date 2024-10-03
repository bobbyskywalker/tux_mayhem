import sys
import pygame

from tux import Tux
from bullet import Bullet

from equipment import Equipment as eq
from random import randint

def check_keyup(event, tux):
    if event.key == pygame.K_w:
        tux.moving_up = False
    elif event.key == pygame.K_s:
        tux.moving_down = False
    elif event.key == pygame.K_a:
        tux.moving_left = False
    elif event.key == pygame.K_d:
        tux.moving_right = False

def check_keydown(event, settings, screen, tux, bullets):
    if event.key == pygame.K_w:
        tux.moving_up = True
    elif event.key == pygame.K_s:
        tux.moving_down = True
    elif event.key == pygame.K_a:
        tux.moving_left = True
    elif event.key == pygame.K_d:
        tux.moving_right = True

def check_events(settings, screen, tux, bullets, angle, eq):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            check_keydown(event, settings, screen, tux, bullets)
        
        if event.type == pygame.KEYUP:
            check_keyup(event, tux)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Fire a bullet
            if eq.ammo > 0:
                new_bullet = Bullet(settings, screen, tux, angle)
                bullets.add(new_bullet)
                eq.drop_ammo()
            
def update_screen(settings, screen, tux, bullets, crosshair, hud, eq, virus):
    # Redraw the screen during each pass through the loop
    current_time = pygame.time.get_ticks()
    screen.blit(settings.bg_img, (0, 0))
    crosshair.update_cursor()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    tux.gather_ammo()
    hud.blit_HUD()
    if eq.ammo_gathered == True:
        eq.ammo_spotx = randint(0, screen.get_width())
        eq.ammo_spoty = randint(0, screen.get_height())
    cords = (eq.ammo_spotx, eq.ammo_spoty)
    if current_time - eq.last_ammo > eq.ammo_spawn_delay:
        screen.blit(eq.ammo_icon, eq.spawn_ammo(cords))
    tux.blitme()
    virus.pursue_player()
    virus.blit_foe()

    # Make the most recently drawn screen visible
    pygame.display.flip()
