import pygame
import time

def get_mouse_pos(choices):
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
                    if mouse_x < 300 and mouse_y < 300:
                        if "1" not in choices:
                            print("Already Taken. Try Again!")
                            mouse_x, mouse_y = get_mouse_pos()
                    elif 300 < mouse_x < 600 and mouse_y < 300:
                        if "2" not in choices:
                            print("Already Taken. Try Again!")
                            mouse_x, mouse_y = get_mouse_pos()
                    elif 600 < mouse_x and mouse_y < 300:
                        if "3" not in choices:
                            print("Already Taken. Try Again!")
                            mouse_x, mouse_y = get_mouse_pos()
                    elif mouse_x < 300 and 300 < mouse_y < 600:
                        if "4" not in choices:
                            print("Already Taken. Try Again!")
                            mouse_x, mouse_y = get_mouse_pos()
                    elif 300 < mouse_x < 600 and 300 < mouse_y < 600:
                        if "5" not in choices:
                            print("Already Taken. Try Again!")
                            mouse_x, mouse_y = get_mouse_pos()
                    elif 600 < mouse_x and 300 < mouse_y < 600:
                        if "6" not in choices:
                            print("Already Taken. Try Again!")
                            mouse_x, mouse_y = get_mouse_pos()
                    elif mouse_x < 300 and 600 < mouse_y:
                        if "7" not in choices:
                            print("Already Taken. Try Again!")
                            mouse_x, mouse_y = get_mouse_pos()
                    elif 300 < mouse_x < 600 and 600 < mouse_y:
                        if "8" not in choices:
                            print("Already Taken. Try Again!")
                            mouse_x, mouse_y = get_mouse_pos()
                    elif 600 < mouse_x and 600 < mouse_y:
                        if "9" not in choices:
                            print("Already Taken. Try Again!")
                            mouse_x, mouse_y = get_mouse_pos()
                    time.sleep(0.5)
                return mouse_x, mouse_y

       