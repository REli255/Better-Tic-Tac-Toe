import pygame

def set_grid():
    pygame.init()

    window_size = (900, 900)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('3x3 Grid')

    screen.fill((155, 200, 255))
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (900, 300), 10)
    pygame.draw.line(screen, (0, 0, 0), (0, 600), (900, 600), 10)
    pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 900), 10)
    pygame.draw.line(screen, (0, 0, 0), (600, 0), (600, 900), 10)

    return screen

set_grid()