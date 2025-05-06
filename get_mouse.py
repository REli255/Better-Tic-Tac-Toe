import pygame
import time
from draw_mark import *
from turns import *

def get_mouse_pos(screen):
    running = True
    turns = 0
    
    while running:
        turn = is_even(turns)
    
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
                    if turn == "Even":
                        draw_x(mouse_x, mouse_y, screen)
                    elif turn == "Odd":
                        draw_o(mouse_x, mouse_y, screen)
                    turns+=1
                time.sleep(0.5)

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

       