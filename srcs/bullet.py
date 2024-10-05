import pygame
from pygame.sprite import Sprite
from math import cos, hypot, sin
import shooting_mechanics as sm

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


class Demon_Bullet(Sprite):
    def __init__(self, settings, screen, tux, demon):
        super().__init__()

        self.tux = tux

        self.demon = demon
        self.screen = screen
        self.settings = settings
        self.rect = pygame.Rect(0, 0, self.settings.demon_bullet_width, self.settings.demon_bullet_height)
        self.rect.top = demon.rect.top
        self.rect.bottom = demon.rect.bottom
        self.rect.left = demon.rect.left
        self.rect.right = demon.rect.right

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.angle = sm.get_angle_between(self.rect, self.tux.rect)

        self.color = settings.demon_bullet_color
        self.speed_factor = settings.demon_bullet_speed_factor

    def update(self):
        self.x += cos(self.angle) * self.settings.demon_bullet_speed_factor
        self.y -= sin(self.angle) * self.settings.demon_bullet_speed_factor
        self.rect.x = self.x
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

def delete_bullets(bullets, HUD):
    for bullet in bullets.copy():
        if (bullet.rect.top) <= HUD.gun_img.get_height() + 5:
            bullets.remove(bullet)
        if (bullet.rect.bottom) >= 1200:
            bullets.remove(bullet)
        if (bullet.rect.left) <= 0:
            bullets.remove(bullet)
        if (bullet.rect.right) >= 1200:
            bullets.remove(bullet)