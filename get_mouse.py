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
                        choices.remove("1")
                    elif 300 < mouse_x < 600 and mouse_y < 300:
                        choices.remove("2")
                    elif 600 < mouse_x and mouse_y < 300:
                        choices.remove("3")
                    elif mouse_x < 300 and 300 < mouse_y < 600:
                        pygame.draw.line(screen, (0, 0, 0), (50, 350), (255,555), 30)
                        pygame.draw.line(screen, (0, 0, 0), (255, 350), (50,555), 30)
                        board[1][0] = "X"
                        choices.remove("4")
                    elif 300 < mouse_x < 600 and 300 < mouse_y < 600:
                        pygame.draw.line(screen, (0, 0, 0), (350, 350), (555,555), 30)
                        pygame.draw.line(screen, (0, 0, 0), (555, 350), (350,555), 30)
                        board[1][1] = "X"
                        choices.remove("5")
                    elif 600 < mouse_x and 300 < mouse_y < 600:
                        pygame.draw.line(screen, (0, 0, 0), (650, 350), (855,555), 30)
                        pygame.draw.line(screen, (0, 0, 0), (855, 350), (650,555), 30)
                        board[1][2] = "X"
                        choices.remove("6")
                    elif mouse_x < 300 and 600 < mouse_y:
                        pygame.draw.line(screen, (0, 0, 0), (50, 650), (255,855), 30)
                        pygame.draw.line(screen, (0, 0, 0), (255, 650), (50,855), 30)
                        board[2][0] = "X"
                        choices.remove("7")
                    elif 300 < mouse_x < 600 and 600 < mouse_y:
                        pygame.draw.line(screen, (0, 0, 0), (350, 650), (555,855), 30)
                        pygame.draw.line(screen, (0, 0, 0), (555, 650), (350,855), 30)
                        board[2][1] = "X"
                        choices.remove("8")
                    elif 600 < mouse_x and 600 < mouse_y:
                        pygame.draw.line(screen, (0, 0, 0), (650, 650), (855,855), 30)
                        pygame.draw.line(screen, (0, 0, 0), (855, 650), (650,855), 30)
                        board[2][2] = "X"
                        choices.remove("9")
                    time.sleep(0.5)
                return mouse_x, mouse_y

       