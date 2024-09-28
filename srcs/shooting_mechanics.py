import pygame
from math import *

def mouse_follow(settings, screen, tux):
    mouse_x, mouse_y = pygame.mouse.get_pos()

def get_angle_between(p1, p2):
    dx = p2[0] - p1[0]
    dy = p1[1] - p2[1]
    angle = atan2(dy, dx)
    return angle
