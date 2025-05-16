import pygame

def set_grid():
    pygame.init()#starts the pygame window

    window_size = (900, 900)#sets the window length and width
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption('3x3 Grid')#Sets the windows name

    screen.fill((155, 200, 255))#lines 10-15 make the grid in the pygame window
    pygame.draw.line(screen, (0, 0, 0), (0, 300), (900, 300), 10)
    pygame.draw.line(screen, (0, 0, 0), (0, 600), (900, 600), 10)
    pygame.draw.line(screen, (0, 0, 0), (300, 0), (300, 900), 10)
    pygame.draw.line(screen, (0, 0, 0), (600, 0), (600, 900), 10)
    pygame.display.flip()

    return screen
