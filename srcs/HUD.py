import pygame
from equipment import Equipment
class HUD:
    def __init__(self, settings, screen, equipment):
        self.screen = screen
        self.settings = settings
        self.equipment = equipment
        self.gun_icon = pygame.image.load("../graphics/gun.bmp")
        self.health_icon = pygame.image.load("../graphics/health.bmp")
        self.score = 0
        self.gun_img = pygame.transform.scale(self.gun_icon, (60, 40))
        self.health_img = pygame.transform.scale(self.health_icon, (30, 30))

        self.health_count = 0
        self.gun_count = 0


    def blit_HUD(self):
        # make up some clever way to print it
        pygame.draw.rect(self.screen, (208, 236, 231), (0, 0, self.screen.get_width(), self.gun_img.get_height() + 5))
        self.screen.blit(self.gun_img, (self.screen.get_width() - self.gun_img.get_width() * 2, 5))
        self.screen.blit(self.health_img, (self.screen.get_width() / 2 - self.health_img.get_width(), 5))
        font = pygame.font.Font(None, self.health_img.get_height())
        text_ammo = font.render('Ammo: ', True, (0, 0, 0)) 
        ammo_val = font.render(str(self.equipment.ammo), True, (0, 0, 0))
        text_health = font.render(': 100', True, (0, 0, 0))
        # print below the gun icon
        self.screen.blit(text_ammo, (10, 10))
        self.screen.blit(ammo_val, (text_ammo.get_width() + 10, 10))
        self.screen.blit(text_health, ((self.screen.get_width() / 2 - self.health_img.get_width()) + self.health_img.get_width() + 10, 10))