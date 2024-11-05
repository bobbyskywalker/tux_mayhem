import sys

import pygame

import srcs.scores as scr


def options(screen):
    rect_play = pygame.Rect(0, 0, 200, 50)
    rect_play.centerx = screen.get_width() / 2
    rect_play.centery = 200

    rect_high_scores = pygame.Rect(0, 0, 200, 50)
    rect_high_scores.centerx = screen.get_width() / 2
    rect_high_scores.centery = screen.get_height() / 4 * 2

    rect_quit = pygame.Rect(0, 0, 200, 50)
    rect_quit.centerx = screen.get_width() / 2
    rect_quit.centery = screen.get_height() / 4 * 3

    return (rect_play, rect_high_scores, rect_quit)


def menu_box(screen):
    color_active = pygame.Color("red")
    color_passive = pygame.Color(96, 96, 96)

    active_play = False
    active_high_scores = False
    active_quit = False

    base_font = pygame.font.Font(None, 60)
    title_surface = base_font.render("TUX MAYHEM", True, (255, 255, 255))
    base_font = pygame.font.Font(None, 24)
    version_surface = base_font.render("v0.99", True, (255, 255, 255))
    base_font = pygame.font.Font(None, 32)
    play_surface = base_font.render("Play", True, (255, 255, 255))
    hs_surface = base_font.render("High Scores", True, (255, 255, 255))
    quit_surface = base_font.render("Quit", True, (255, 255, 255))

    rect_play, rect_high_scores, rect_quit = options(screen)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if active_play:
                    return 1
                if active_high_scores:
                    display = True
                    while display:
                        scores = scr.get_scores()
                        display = scr.display_scores(screen, scores)
                if active_quit:
                    pygame.quit()
                    sys.exit()
            else:
                if rect_play.collidepoint(mouse_pos):
                    active_play = True
                else:
                    active_play = False
                if rect_high_scores.collidepoint(mouse_pos):
                    active_high_scores = True
                else:
                    active_high_scores = False
                if rect_quit.collidepoint(mouse_pos):
                    active_quit = True
                else:
                    active_quit = False

        screen.fill(("lightskyblue3"))

        if active_play:
            pygame.draw.rect(screen, color_active, rect_play)
        else:
            pygame.draw.rect(screen, color_passive, rect_play)

        if active_high_scores:
            pygame.draw.rect(screen, color_active, rect_high_scores)
        else:
            pygame.draw.rect(screen, color_passive, rect_high_scores)

        if active_quit:
            pygame.draw.rect(screen, color_active, rect_quit)
        else:
            pygame.draw.rect(screen, color_passive, rect_quit)

        screen.blit(
            title_surface,
            (
                screen.get_width() / 2 - title_surface.get_width() / 2,
                screen.get_height() / 10,
            ),
        )
        screen.blit(
            version_surface,
            (
                screen.get_width() / 2 - version_surface.get_width() / 2,
                screen.get_height() / 10 + 50,
            ),
        )
        screen.blit(
            play_surface,
            (
                rect_play.x + rect_play.width / 2 - play_surface.get_width() / 2,
                rect_play.y + 5,
            ),
        )
        screen.blit(
            hs_surface,
            (
                rect_high_scores.x
                + rect_high_scores.width / 2
                - hs_surface.get_width() / 2,
                rect_high_scores.y + 5,
            ),
        )
        screen.blit(
            quit_surface,
            (
                rect_quit.x + rect_quit.width / 2 - quit_surface.get_width() / 2,
                rect_quit.y + 5,
            ),
        )
        pygame.display.flip()
