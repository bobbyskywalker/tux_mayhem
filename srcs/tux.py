import pygame
from HUD import HUD
class Tux():
    def __init__(self, screen, HUD, eq):
        self.screen = screen
        self.og_image = pygame.image.load("../graphics/tux.bmp")
        self.image = pygame.transform.scale(self.og_image, (60, 60))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # hero cords
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.hud = HUD

        self.eq = eq
        
    def update_pos(self):
        if self.moving_up and self.rect.top > self.hud.gun_img.get_height():
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1  
        if self.moving_left and self.rect.centerx > 0:
            self.rect.centerx -= 1
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.rect.centerx += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def gather_ammo(self):
        if self.rect.colliderect(self.eq.ammo_rect) and not self.eq.ammo_gathered:
            overlap_rect = self.rect.clip(self.eq.ammo_rect)

            tux_mask = pygame.mask.from_surface(self.image)
            ammo_mask = pygame.mask.from_surface(self.eq.ammo_icon)

            offset = (overlap_rect.x - self.rect.x, overlap_rect.y - self.rect.y)
            if tux_mask.overlap(ammo_mask, offset):
                    self.eq.last_ammo = pygame.time.get_ticks()
                    self.eq.ammo += 10
                    self.eq.ammo_gathered = True
