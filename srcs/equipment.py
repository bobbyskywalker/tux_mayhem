import pygame
from random import randint
class Equipment():
    def __init__(self, screen):
        self.screen = screen
        self.ammo = 5
        self.health = 0
        self.current_weapon = 'GUN'
        self.ammo_gathered = False
        self.ammo_icon_og = pygame.image.load("../graphics/ammo.bmp")
        self.ammo_icon = pygame.transform.scale(self.ammo_icon_og, (30, 30))
        self.ammo_rect = self.ammo_icon.get_rect()

        self.ammo_spotx = randint(0, screen.get_width())
        self.ammo_spoty = randint(0, screen.get_height())

        #last ammo- time since the last gather
        self.ammo_spawn_delay = 5000
        self.last_ammo = -1000000

    def drop_ammo(self):
        self.ammo -= 1

    def spawn_ammo(self, cords):
        coords = (cords[0], cords[1])
        self.ammo_rect.topleft = coords
        self.ammo_gathered = False
        return coords
