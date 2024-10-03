import pygame
import math


# TODO:
# remove tux health on collision (1 second collsion == -20 hp)
# add bullet collision, then decrease foe health
# health bar down below- 3 hits
# if health == 0, delete from the group
class Virus_foe():
    def __init__(self, screen, tux):
        self.screen = screen

        self.og_image = pygame.image.load("../graphics/viurs.bmp")
        self.image = pygame.transform.scale(self.og_image, (100, 50))
        self.rect = self.image.get_rect()

        self.speed = 1

        self.tux = tux

        self.health = 100

    def blit_foe(self):
        self.screen.blit(self.image, self.rect)

    def pursue_player(self):
        dx, dy = self.tux.rect.x - self.rect.x, self.tux.rect.y - self.rect.y
        dst = math.hypot(dx, dy)
        if not dx == 0 and not dx == 0:
            dx, dy = dx / dst, dy / dst
        self.rect.centerx += dx * self.speed
        self.rect.centery += dy  * self.speed


    # def pursue_player(self):
    #     # Find direction vector (dx, dy) between enemy and self.tux.
    #     dirvect = pygame.math.Vector2(self.tux.rect.x - self.rect.x,
    #                                     self.tux.rect.y - self.rect.y)
    #     dirvect.normalize()
    #     # Move along this normalized vector towards the self.tux at current speed.
    #     dirvect.scale_to_length(self.speed)
    #     self.rect.move_ip