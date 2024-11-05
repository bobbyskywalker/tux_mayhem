from math import atan2

import pygame


class Cursor:
    def __init__(self, screen):
        self.cursor_img_og = pygame.image.load("../graphics/crosshair.bmp")
        self.cursor_img = pygame.transform.scale(self.cursor_img_og, (20, 20))
        self.cursor_img_rect = self.cursor_img.get_rect()
        self.cursor_img_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
        self.screen = screen

    def update_cursor(self):
        self.cursor_img_rect.center = pygame.mouse.get_pos()
        self.screen.blit(self.cursor_img, self.cursor_img_rect)


def get_angle_between(p1, p2):
    dx = p2[0] - p1[0]
    dy = p1[1] - p2[1]
    angle = atan2(dy, dx)
    return angle
