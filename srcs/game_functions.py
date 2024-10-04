import sys
import pygame
from tux import Tux
from bullet import Bullet
from equipment import Equipment as eq
from random import randint
from enemies import *

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

def check_events(settings, screen, tux, bullets, angle, eq, virus):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            check_keydown(event, settings, screen, tux, bullets)
        
        if event.type == pygame.KEYUP:
            check_keyup(event, tux)
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if eq.ammo > 0:
                new_bullet = Bullet(settings, screen, tux, angle)
                bullets.add(new_bullet)
                eq.drop_ammo()

def update_foes(viruses, skulls, demons, hud, current_time):
    for virus in viruses.sprites():
        virus.take_damage()
        if current_time - virus.last_hit > virus.hit_delay:
            virus.give_damage()
        virus.pursue_player()
        if virus.health > 0:
            virus.blit_foe()
        else:
            hud.score += 100
            virus.remove(viruses)

    for skull in skulls.sprites():
        skull.take_damage()
        if current_time - skull.last_hit > skull.hit_delay:
            skull.give_damage()
        skull.pursue_player()
        if skull.health > 0:
            skull.blit_foe()
        else:
            hud.score += 200
            skull.remove(skulls)

    for demon in demons.sprites():
        demon.take_damage()
        if current_time - demon.last_hit > demon.hit_delay:
            demon.give_damage()
        demon.pursue_player()
        if demon.health > 0:
            demon.blit_foe()
        else:
            hud.score += 500
            demon.remove(demons)
def update_screen(settings, screen, tux, bullets, crosshair, hud, eq, viruses, skulls, demons):
    current_time = pygame.time.get_ticks()
    screen.blit(settings.bg_img, (0, 0))
    crosshair.update_cursor()
    # bullets update
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #tux update
    tux.gather_ammo()
    tux.blitme()
    # hud update
    hud.blit_HUD()
    #ammo update
    if eq.ammo_gathered == True:
        eq.ammo_spotx = randint(eq.ammo_icon.get_width(), screen.get_width() - eq.ammo_icon.get_width())
        eq.ammo_spoty = randint(10 + hud.gun_img.get_height(), screen.get_height() - eq.ammo_icon.get_height())
    cords = (eq.ammo_spotx, eq.ammo_spoty)
    if current_time - eq.last_ammo > eq.ammo_spawn_delay:
        screen.blit(eq.ammo_icon, eq.spawn_ammo(cords))

    #foe update
    update_foes(viruses, skulls, demons, hud, current_time)

    pygame.display.flip()

def game_over(screen):
    while 1:
        font = pygame.font.Font(None, 100)
        game_over = font.render('YOU DIED', True, (255, 100, 100))
        font = pygame.font.Font(None, 20)
        press_key = font.render('Press any key to exit', True, (0, 0, 0))
        screen.blit(game_over, (screen.get_width() / 2 - game_over.get_width() / 2, screen.get_height() / 2 - game_over.get_height() / 2))
        screen.blit(press_key, (screen.get_width() / 2 - press_key.get_width() / 2, screen.get_height() / 2 + game_over.get_height() / 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                sys.exit()  