import pygame
from pygame.sprite import Sprite

#TODO: make bullets fire according to crosshair
# and ofc add crosshair :pp
class Bullet(Sprite):
    def __init__(self, settings, screen, tux):
        super().__init__()

        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = tux.rect.centerx
        self.rect.top = tux.rect.top

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = settings.bullet_color
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        self.x += self.speed_factor
        self.y -= self.speed_factor
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
