import pygame


    
def draw_x(mouse_x,mouse_y,screen):
    if mouse_x < 300 and mouse_y < 300:
        pygame.draw.line(screen, (0, 0, 0), (50, 50), (255,255), 30)
        pygame.draw.line(screen, (0, 0, 0), (255, 50), (50,255), 30)
    elif 300 < mouse_x < 600 and mouse_y < 300:
        pygame.draw.line(screen, (0, 0, 0), (350, 50), (555,255), 30)
        pygame.draw.line(screen, (0, 0, 0), (555, 50), (350,255), 30)
    elif 600 < mouse_x and mouse_y < 300:
        pygame.draw.line(screen, (0, 0, 0), (650, 50), (855,255), 30)
        pygame.draw.line(screen, (0, 0, 0), (855, 50), (650,255), 30)
    elif mouse_x < 300 and 300 < mouse_y < 600:
        pygame.draw.line(screen, (0, 0, 0), (50, 350), (255,555), 30)
        pygame.draw.line(screen, (0, 0, 0), (255, 350), (50,555), 30)
    elif 300 < mouse_x < 600 and 300 < mouse_y < 600:
        pygame.draw.line(screen, (0, 0, 0), (350, 350), (555,555), 30)
        pygame.draw.line(screen, (0, 0, 0), (555, 350), (350,555), 30)
    elif 600 < mouse_x and 300 < mouse_y < 600:
        pygame.draw.line(screen, (0, 0, 0), (650, 350), (855,555), 30)
        pygame.draw.line(screen, (0, 0, 0), (855, 350), (650,555), 30)
    elif mouse_x < 300 and 600 < mouse_y:
        pygame.draw.line(screen, (0, 0, 0), (50, 650), (255,855), 30)
        pygame.draw.line(screen, (0, 0, 0), (255, 650), (50,855), 30)
    elif 300 < mouse_x < 600 and 600 < mouse_y:
        pygame.draw.line(screen, (0, 0, 0), (350, 650), (555,855), 30)
        pygame.draw.line(screen, (0, 0, 0), (555, 650), (350,855), 30)
    elif 600 < mouse_x and 600 < mouse_y:
        pygame.draw.line(screen, (0, 0, 0), (650, 650), (855,855), 30)
        pygame.draw.line(screen, (0, 0, 0), (855, 650), (650,855), 30)
    pygame.display.flip()
   


def draw_o(mouse_x,mouse_y,screen):
    if mouse_x < 300 and mouse_y < 300:
        pygame.draw.circle(screen, (0, 0, 0), (150, 150), 120, width=20, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)
    elif 300 < mouse_x < 600 and mouse_y < 300:
        pygame.draw.circle(screen, (0, 0, 0), (450, 150), 120, width=20, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)
    elif 600 < mouse_x and mouse_y < 300:
        pygame.draw.circle(screen, (0, 0, 0), (750, 150), 120, width=20, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)
    elif mouse_x < 300 and 300 < mouse_y < 600:
        pygame.draw.circle(screen, (0, 0, 0), (150, 450), 120, width=20, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)
    elif 300 < mouse_x < 600 and 300 < mouse_y < 600:
        pygame.draw.circle(screen, (0, 0, 0), (450, 450), 120, width=20, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)
    elif 600 < mouse_x and 300 < mouse_y < 600:
       pygame.draw.circle(screen, (0, 0, 0), (750, 450), 120, width=20, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)
    elif mouse_x < 300 and 600 < mouse_y:
        pygame.draw.circle(screen, (0, 0, 0), (150, 750), 120, width=20, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)
    elif 300 < mouse_x < 600 and 600 < mouse_y:
       pygame.draw.circle(screen, (0, 0, 0), (450, 750), 120, width=20, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)
    elif 600 < mouse_x and 600 < mouse_y:
        pygame.draw.circle(screen, (0, 0, 0), (750, 750), 120, width=20, draw_top_right=1, draw_top_left=1, draw_bottom_left=1, draw_bottom_right=1)
    pygame.display.flip()