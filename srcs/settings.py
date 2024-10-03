import pygame

class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800

        self.bg = pygame.image.load("../graphics/background.bmp")
        self.bg_img = pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))
        self.bg_color = (255, 255, 255)

        self.tux_speed_factor = 2
        #bullets
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (0 , 0, 0)
