import sys
import pygame

from tux import Tux
from bullet import Bullet

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

def check_events(settings, screen, tux, bullets, angle):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            check_keydown(event, settings, screen, tux, bullets)
        
        if event.type == pygame.KEYUP:
            check_keyup(event, tux)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Fire a bullet
            new_bullet = Bullet(settings, screen, tux, angle)
            bullets.add(new_bullet)
            
def update_screen(settings, screen, tux, bullets, crosshair, hud):
    # Redraw the screen during each pass through the loop
    screen.fill(settings.bg_color)

    crosshair.update_cursor()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    tux.blitme()
    hud.blit_HUD()
    # Make the most recently drawn screen visible
    pygame.display.flip()
