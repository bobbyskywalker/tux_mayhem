import pygame
from pygame.sprite import Sprite
from math import *

#TODO: make bullets fire according to crosshair
# and ofc add crosshair :pp
# one bullet allowed
class Bullet(Sprite):
    def __init__(self, settings, screen, tux, angle):
        super().__init__()

        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.top = tux.rect.top
        self.rect.bottom = tux.rect.bottom
        self.rect.left = tux.rect.left
        self.rect.right = tux.rect.right

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.angle = angle

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        self.x += cos(self.angle) * self.speed_factor
        self.y -= sin(self.angle) * self.speed_factor
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def delete_bullets(bullets):
    for bullet in bullets.copy():
        if (bullet.rect.top) <= 0:
            bullets.remove(bullet)
        if (bullet.rect.bottom) >= 1200:
            bullets.remove(bullet)
        if (bullet.rect.left) <= 0:
            bullets.remove(bullet)
        if (bullet.rect.right) >= 1200:
            bullets.remove(bullet)