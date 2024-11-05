import pygame

from srcs.equipment import Equipment


class HUD:
    def __init__(self, settings, screen, equipment):
        self.screen = screen
        self.settings = settings
        self.equipment = equipment
        self.gun_icon = pygame.image.load("graphics/gun.bmp")
        self.rifle_icon = pygame.image.load("graphics/rifle.bmp")
        self.health_icon = pygame.image.load("graphics/health.bmp")
        self.score = 0
        self.rifle_img = pygame.transform.scale(self.rifle_icon, (100, 40))
        self.gun_img = pygame.transform.scale(self.gun_icon, (60, 40))
        self.health_img = pygame.transform.scale(self.health_icon, (30, 30))
        self.health_count = 0
        self.gun_count = 0

        self.wave = 1

        self.score = 0

    def blit_HUD(self):
        # make up some clever way to print it
        pygame.draw.rect(
            self.screen,
            (208, 236, 231),
            (0, 0, self.screen.get_width(), self.gun_img.get_height() + 5),
        )
        if self.equipment.current_weapon == "GUN":
            self.screen.blit(
                self.gun_img,
                (self.screen.get_width() - self.gun_img.get_width() * 2, 5),
            )
        else:
            self.screen.blit(
                self.rifle_img,
                (self.screen.get_width() - self.gun_img.get_width() * 2, 5),
            )

        self.screen.blit(
            self.health_img,
            (self.screen.get_width() / 2 - self.health_img.get_width(), 5),
        )
        font = pygame.font.Font(None, self.health_img.get_height())
        text_ammo = font.render("Ammo: " + str(self.equipment.ammo), True, (0, 0, 0))
        text_score = font.render("Score: " + str(self.score), True, (0, 0, 214))
        health_val = font.render(": " + str(self.equipment.health), True, (0, 0, 0))
        wave_val = font.render("Wave: " + str(self.wave), True, (0, 0, 214))
        self.screen.blit(text_ammo, (10, 10))
        self.screen.blit(
            text_score, (self.screen.get_width() / 4 - text_score.get_width(), 10)
        )
        self.screen.blit(
            wave_val,
            (
                self.screen.get_width() / 2
                + self.screen.get_width() / 4
                - wave_val.get_width(),
                10,
            ),
        )
        self.screen.blit(
            health_val,
            (
                (
                    self.screen.get_width() / 2
                    - self.health_img.get_width()
                    + self.health_img.get_width()
                    + 10
                ),
                10,
            ),
        )
