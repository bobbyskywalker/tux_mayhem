import pygame
import sys
class Shop():
    def __init__(self, screen, hud, eq, tux):
        self.tux = tux
        self.screen = screen
        self.hud = hud
        self.eq = eq
        self.shop_start = self.screen.get_width() / 4
        self.shop_end = self.screen.get_height() / 4
        self.shop_width = self.screen.get_width() / 2
        self.shop_height = self.screen.get_height() / 2

        self.active = False

    def print_shop(self, purchased_items):
        pygame.draw.rect(self.screen, (229, 204, 255), (self.shop_start, self.shop_end, self.shop_width, self.shop_height))
        font = pygame.font.Font(None, 30)
        
        wave_info = font.render('Wave completed! Use score to buy stuff!', True, (0, 0, 0))
        buy_ammo = font.render('1. 50 bullets: -100 score', True, (0, 76, 153))
        buy_health = font.render('2. Refill health: -500 score', True, (0, 76, 153))
        buy_rifle = font.render('3. Automatic rifle: -3000 score', True, (0, 76, 153))
        font = pygame.font.Font(None, 25)
        exit_info = font.render('(Press q to exit)', True, (0, 0, 0))

        self.screen.blit(wave_info, (self.shop_start + 100, self.shop_end + 10))
        self.screen.blit(buy_ammo, (self.shop_start + 100, self.shop_end + 100))
        self.screen.blit(buy_health, (self.shop_start + 100, self.shop_end + 200))
        self.screen.blit(buy_rifle, (self.shop_start + 100, self.shop_end + 300))
        self.screen.blit(exit_info, (self.shop_start + 100, self.shop_end + 350))

        purchased_info = font.render('Purchased!', True, (255, 0, 0))

        if purchased_items[0] == True:
            self.screen.blit(purchased_info, (self.shop_start + 500, self.shop_end + 100))
        if purchased_items[1] == True:
            self.screen.blit(purchased_info, (self.shop_start + 500, self.shop_end + 200))
        if purchased_items[2] == True:
            self.screen.blit(purchased_info, (self.shop_start + 500, self.shop_end + 300))
        pygame.display.flip()
    
    def buy_items(self):
        # 0 = bullets, 1 = health, 2 = rifle
        purchased_items = [False, False, False]
        while self.active:
            self.print_shop(purchased_items)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        if self.hud.score >= 100:
                            purchased_items[0] = True
                            self.hud.score -= 100
                            self.eq.ammo += 50
                    elif event.key == pygame.K_2:
                        if self.hud.score >= 500:
                            purchased_items[1] = True
                            self.hud.score -= 500
                            self.eq.health = 100
                    elif event.key == pygame.K_3:
                        if self.hud.score >= 3000:
                            purchased_items[2] = True
                            self.hud.score -= 3000
                            self.eq.current_weapon = 'RIFLE'
                    elif event.key == pygame.K_q:
                        self.active = False
                self.hud.blit_HUD()
                pygame.display.flip()

        # bug duck tape fix lol
        self.tux.moving_up = False
        self.tux.moving_down = False
        self.tux.moving_left = False
        self.tux.moving_right = False