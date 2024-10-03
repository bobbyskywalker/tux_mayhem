import sys
import pygame
from tux import Tux
from bullet import Bullet
from equipment import Equipment as eq
from random import randint
from enemies import Virus_foe

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
            
def update_screen(settings, screen, tux, bullets, crosshair, hud, eq, viruses):
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
        eq.ammo_spoty = randint(0 + hud.gun_img.get_height(), screen.get_height() - eq.ammo_icon.get_height())
    cords = (eq.ammo_spotx, eq.ammo_spoty)
    if current_time - eq.last_ammo > eq.ammo_spawn_delay:
        screen.blit(eq.ammo_icon, eq.spawn_ammo(cords))

    #foe update
    for virus in viruses.sprites():
        if isinstance(virus, Virus_foe):
            virus.take_damage()
    for virus in viruses.sprites():
        if current_time - virus.last_hit > virus.hit_delay:
            virus.give_damage()
        virus.pursue_player()
        if virus.health > 0:
            virus.blit_foe()
        else:
            virus.remove(viruses)

    pygame.display.flip()

def game_over(screen):
    while 1:
        pygame.display.flip()
        font = pygame.font.Font(None, 100)
        game_over = font.render('YOU DIED', True, (255, 100, 100))
        font = pygame.font.Font(None, 20)
        press_key = font.render('Press any key to exit', True, (0, 0, 0))
        screen.blit(game_over, (screen.get_width() / 2 - game_over.get_width() / 2, screen.get_height() / 2 - game_over.get_height() / 2))
        screen.blit(press_key, (screen.get_width() / 2 - press_key.get_width() / 2, screen.get_height() / 2 + game_over.get_height() / 2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                sys.exit()  