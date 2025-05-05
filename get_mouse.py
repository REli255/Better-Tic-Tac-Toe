import pygame
import time
from draw_mark import *

def get_mouse_pos(screen):
    running = True
    turn = False
    turns = 0
    

    def is_even(turns):
        if (turns%2) == 0:
            turn = True
        else:
            turn = False
        return turn
    
    while running:
        turn = is_even(turns)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            time.sleep(400)
            if event.type == pygame.MOUSEBUTTONUP:
                print('Mouse button pressed!')

        #if event.type == pygame.MOUSEBUTTONDOWN:
            #if event.type == pygame.MOUSEBUTTONUP:
                #mouse_x, mouse_y = event.pos
                #if mouse_x == 300 or mouse_x == 600 or mouse_x == 900 or mouse_y == 300 or mouse_y == 600 or mouse_y == 900:
                    #print("Click in a square not on the edges to play")
                    #mouse_x, mouse_y = get_mouse_pos()
                #else:
                    #if turn == True:
                        #draw_x(mouse_x, mouse_y, screen)
                    #elif turn == False:
                        #draw_o(mouse_x, mouse_y, screen)
                    #turn+=1

       