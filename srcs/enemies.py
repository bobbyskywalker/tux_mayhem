import pygame
import math
from random import randint
from pygame.sprite import Sprite

class Virus_foe(Sprite):
    def __init__(self, screen, tux, bullets, eq):
        super().__init__()
        self.screen = screen

        self.og_image = pygame.image.load("../graphics/viurs.bmp")
        self.image = pygame.transform.scale(self.og_image, (100, 50))
        self.rect = self.image.get_rect()

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
        self.screen.blit(health_str, (self.rect.centerx - health_str.get_width() / 2, self.rect.top - health_str.get_height()))
        self.screen.blit(self.image, self.rect)

    def pursue_player(self):
        dx, dy = self.tux.rect.x - self.rect.x, self.tux.rect.y - self.rect.y
        dst = math.hypot(dx, dy)
        if dst > 0:
            dx, dy = dx / dst, dy / dst
            self.rect.centerx += dx * self.speed
            self.rect.centery += dy  * self.speed

    # def delete_enemy(self):
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
        
def spawn_foes(viruses, screen, tux, bullets, eq):
    for _ in range(5):
        virus = Virus_foe(screen, tux, bullets, eq)
        virus.rect.x = randint(0, screen.get_width() - virus.rect.width)
        virus.rect.y = randint(0, screen.get_height() - virus.rect.height)
        viruses.add(virus)