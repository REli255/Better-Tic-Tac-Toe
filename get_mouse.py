import pygame
import time



def get_mouse_pos():
    running = True
    
    while running:# makes sure the x and y cordinates are gotten before stopping the function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:#gets the x and y cordinates in the window if the mouse is clicked
                mouse_x, mouse_y = event.pos
                if mouse_x == 300 or mouse_x == 600 or mouse_x == 900 or mouse_y == 300 or mouse_y == 600 or mouse_y == 900:# makes sure the user does not click on the grid lines
                    print("Click in a square not on the edges to play")
                else:
                    time.sleep(0.5)#just a delay so things dont appear to fast
                    return mouse_x, mouse_y

       