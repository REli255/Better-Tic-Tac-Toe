import pygame
import time

def get_mouse_pos():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
                print('Mouse button pressed!')
                mouse_x, mouse_y = event.pos
                if mouse_x == 300 or mouse_x == 600 or mouse_x == 900 or mouse_y == 300 or mouse_y == 600 or mouse_y == 900:
                    print("Click in a square not on the edges to play")
                    mouse_x, mouse_y = get_mouse_pos()
                else:
                    time.sleep(0.5)
                return mouse_x, mouse_y

       