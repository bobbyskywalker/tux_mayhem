import pygame

class HUD:
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings

        self.gun_icon = pygame.image.load("../graphics/gun.bmp")
        self.health_icon = pygame.image.load("../graphics/health.bmp")
        self.score = 0
        self.gun_img = pygame.transform.scale(self.gun_icon, (60, 40))
        self.health_img = pygame.transform.scale(self.health_icon, (30, 30))

        self.health_count = 0
        self.gun_count = 0


    def blit_HUD(self):
        # make up some clever way to print it
        self.screen.blit(self.gun_img, (20, 20))
        self.screen.blit(self.health_img, (self.screen.get_width() / 2 - self.health_img.get_width(), 5))
        font = pygame.font.Font(None, 36)
        text_surface = font.render('Ammo: 30', True, (0, 0, 0)) 
        # print below the gun icon
        self.screen.blit(text_surface, (10, 10))