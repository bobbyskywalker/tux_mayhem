import math
from random import randint

import pygame
from pygame.sprite import Sprite

from bullet import Demon_Bullet


# generic motherclass
class Enemy(Sprite):
    def __init__(self, screen, tux, bullets, eq):
        super().__init__()
        self.screen = screen

        self.image = None
        self.rect = None

        self.speed = 1

        self.tux = tux
        self.bullets = bullets

        self.health = 100

        self.eq = eq

        self.hit_delay = 2000
        self.last_hit = 0

    def blit_foe(self):
        font = pygame.font.Font(None, self.image.get_height() // 2)
        health_str = font.render(str(self.health), True, (255, 0, 0))
        self.screen.blit(
            health_str,
            (
                self.rect.centerx - health_str.get_width() / 2,
                self.rect.top - health_str.get_height(),
            ),
        )
        self.screen.blit(self.image, self.rect)

    # collision handled with 'repulsion force', shit took me too much time :DD
    def pursue_player(self, all_enemies):
        dx, dy = self.tux.rect.x - self.rect.x, self.tux.rect.y - self.rect.y
        dst = math.hypot(dx, dy)

        if dst > 0:
            dx, dy = dx / dst, dy / dst

        move_x, move_y = dx * self.speed, dy * self.speed

        min_distance = 50
        repulsion_strength = 1.5

        for enemy in all_enemies:
            if enemy != self:
                distance = math.hypot(
                    enemy.rect.centerx - self.rect.centerx,
                    enemy.rect.centery - self.rect.centery,
                )
                if distance < min_distance:
                    # Calculate the repulsion force direction (push away from the other enemy)
                    repulse_dx = self.rect.centerx - enemy.rect.centerx
                    repulse_dy = self.rect.centery - enemy.rect.centery
                    repulse_dist = math.hypot(repulse_dx, repulse_dy)

                    if repulse_dist > 0:
                        repulse_dx /= repulse_dist
                        repulse_dy /= repulse_dist
                        move_x += repulse_dx * repulsion_strength
                        move_y += repulse_dy * repulsion_strength

        self.rect.centerx += int(move_x)
        self.rect.centery += int(move_y)

    def take_damage(self):
        for bullet in self.bullets.sprites():
            if self.rect.colliderect(bullet.rect):
                self.health -= 20
                self.bullets.remove(bullet)

    def give_damage(self):
        current_time = pygame.time.get_ticks()
        if self.rect.colliderect(self.tux.rect):
            self.eq.health -= 5
            self.last_hit = current_time


class Skull_foe(Enemy):
    def __init__(self, screen, tux, bullets, eq):
        super().__init__(screen, tux, bullets, eq)
        self.og_image = pygame.image.load("../graphics/skull.bmp")
        self.image = pygame.transform.scale(self.og_image, (50, 50))
        self.rect = self.image.get_rect()
        self.speed = 4
        self.health = 40
        self.hit_delay = 2000
        self.last_hit = 0


class Virus_foe(Enemy):
    def __init__(self, screen, tux, bullets, eq):
        super().__init__(screen, tux, bullets, eq)
        self.og_image = pygame.image.load("../graphics/viurs.bmp")
        self.image = pygame.transform.scale(self.og_image, (100, 50))
        self.rect = self.image.get_rect()
        self.speed = 3
        self.health = 100
        self.hit_delay = 2000
        self.last_hit = 0


class Demon_foe(Enemy):
    def __init__(self, screen, tux, bullets, eq, settings):
        super().__init__(screen, tux, bullets, eq)
        self.og_image = pygame.image.load("../graphics/demon.bmp")
        self.image = pygame.transform.scale(self.og_image, (100, 50))
        self.rect = self.image.get_rect()
        self.speed = 3
        self.health = 200
        self.hit_delay = 2000
        self.shoot_delay = 500
        self.last_shot = 0
        self.last_hit = 0
        self.settings = settings
        self.demon_bullets = pygame.sprite.Group()

    def shoot(self):
        bullet = Demon_Bullet(self.settings, self.screen, self.tux, self)
        self.demon_bullets.add(bullet)

    def take_bullet_damage(self):
        for bullet in self.demon_bullets.sprites():
            if bullet.rect.colliderect(self.tux.rect):
                self.eq.health -= 5
                self.demon_bullets.remove(bullet)


class Boss_foe(Demon_foe):
    def __init__(self, screen, tux, bullets, eq, settings):
        super().__init__(screen, tux, bullets, eq, settings)
        self.og_image = pygame.image.load("../graphics/bear_boss.bmp")
        self.image = pygame.transform.scale(self.og_image, (150, 125))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 100
        self.speed = 4
        self.health = 2000
        self.hit_delay = 2000
        self.shoot_delay = 200
        self.last_shot = 0
        self.last_hit = 0
        self.settings = settings
        self.alive = False
        # flag to raise score once
        self.killed = False
        self.demon_bullets = pygame.sprite.Group()

    def shoot(self):
        bullet = Demon_Bullet(self.settings, self.screen, self.tux, self)
        self.demon_bullets.add(bullet)

    def take_bullet_damage(self):
        for bullet in self.demon_bullets.sprites():
            if bullet.rect.colliderect(self.tux.rect):
                self.eq.health -= 5
                self.demon_bullets.remove(bullet)


def spawn_foes(viruses, skulls, demons, screen, tux, bullets, eq, hud, settings, boss):
    match hud.wave:
        case 1:
            num_virus = 5
            num_skull = 0
            num_demons = 0
        case 2:
            num_virus = 0
            num_skull = 2
            num_demons = 0
        case 3:
            num_virus = 3
            num_skull = 3
            num_demons = 0
        case 4:
            num_virus = 0
            num_skull = 0
            num_demons = 3
        case 5:
            num_virus = 2
            num_skull = 2
            num_demons = 2
        case 6:
            num_virus = 3
            num_skull = 3
            num_demons = 3
        case 7:
            num_virus = 2
            num_skull = 2
            num_demons = 5
        case 8:
            num_virus = 3
            num_skull = 5
            num_demons = 4
        case 9:
            num_virus = 5
            num_skull = 5
            num_demons = 5
        case 10:
            num_virus = 3
            num_skull = 3
            num_demons = 3

    safe_zone_x = screen.get_width() * 0.3
    safe_zone_y = screen.get_height() * 0.3
    safe_zone_width = screen.get_width() * 0.5
    safe_zone_height = screen.get_height() * 0.5

    for _ in range(num_virus):
        virus = Virus_foe(screen, tux, bullets, eq)
        while True:
            virus.rect.x = randint(0, screen.get_width() - virus.rect.width)
            virus.rect.y = randint(100, screen.get_height() - virus.rect.height)
            if (
                virus.rect.x < safe_zone_x
                or virus.rect.x > safe_zone_x + safe_zone_width
                or virus.rect.y < safe_zone_y
                or virus.rect.y > safe_zone_y + safe_zone_height
            ):
                break
        viruses.add(virus)  
    for _ in range(num_skull):
        skull = Skull_foe(screen, tux, bullets, eq)
        while True:
            skull.rect.x = randint(0, screen.get_width() - skull.rect.width)
            skull.rect.y = randint(100, screen.get_height() - skull.rect.height)
            if (
                skull.rect.x < safe_zone_x
                or skull.rect.x > safe_zone_x + safe_zone_width
                or skull.rect.y < safe_zone_y
                or skull.rect.y > safe_zone_y + safe_zone_height
            ):
                break
        skulls.add(skull)

    for _ in range(num_demons):
        demon = Demon_foe(screen, tux, bullets, eq, settings)
        while True:
            demon.rect.x = randint(0, screen.get_width() - demon.rect.width)
            demon.rect.y = randint(100, screen.get_height() - demon.rect.height)
            if (
                demon.rect.x < safe_zone_x
                or demon.rect.x > safe_zone_x + safe_zone_width
                or demon.rect.y < safe_zone_y
                or demon.rect.y > safe_zone_y + safe_zone_height
            ):
                break
        demons.add(demon)
