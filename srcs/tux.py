import pygame

class Tux():
    def __init__(self, screen):
        self.screen = screen
        self.og_image = pygame.image.load("graphics/tux.bmp")
        self.image = pygame.transform.scale(self.og_image, (60, 60))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # hero cords
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.rect.top = self.screen_rect.top
        self.rect.right = self.screen_rect.right
        self.rect.left = self.screen_rect.left

        # movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False


    def update_pos(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1  
        if self.moving_left and self.rect.centerx > 0:
            self.rect.centerx -= 1
        if self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.rect.centerx += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

