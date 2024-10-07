import pygame
import sys
import time

def input_box(screen):
    user_text = ""

    input_rect = pygame.Rect(screen.get_width() / 2 - 75, screen.get_height() / 4, 300, 50)

    color_active = pygame.Color("lightskyblue3")
    color_passive = pygame.Color("blue")
    color = color_passive

    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:

                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    saved = base_font.render('saved!', True, (255, 255, 255))
                    screen.blit(saved, (screen.get_width() / 2 - saved.get_width() / 2, screen.get_height() / 2 - saved.get_height() / 2))
                    pygame.display.flip()
                    time.sleep(2)
                    return user_text
                else:
                    user_text += event.unicode

        screen.fill((0, 76, 153))

        if active:
            color = color_active
        else:
            color = color_passive

        pygame.draw.rect(screen, color, input_rect)
        base_font = pygame.font.Font(None, 32)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        base_font = pygame.font.Font(None, 25)
        info_text = base_font.render('Enter your name (enter to accept) :', True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        screen.blit(info_text, (input_rect.x - 80, input_rect.y - 70))
        input_rect.w = max(100, text_surface.get_width() + 10)
        pygame.display.flip()

def save_score(score, screen):
    with open("../score.txt", "a") as f:
        f.write(',' + input_box(screen) + ',' + str(score))
        f.close()
        
