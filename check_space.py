
from get_mouse import get_mouse_pos

def check_space(mouse_x, mouse_y, choices):#checks the space the user chose and if it is taken the user needs to choose a different one 
    if mouse_x < 300 and mouse_y < 300:
        if "1" not in choices:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif 300 < mouse_x < 600 and mouse_y < 300:
        if "2" not in choices:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif 600 < mouse_x and mouse_y < 300:
        if "3" not in choices:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif mouse_x < 300 and 300 < mouse_y < 600:
        if "4" not in choices:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif 300 < mouse_x < 600 and 300 < mouse_y < 600:
        if "5" not in choices:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif 600 < mouse_x and 300 < mouse_y < 600:
        if "6" not in choices:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif mouse_x < 300 and 600 < mouse_y:
        if "7" not in choices:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif 300 < mouse_x < 600 and 600 < mouse_y:
        if "8" not in choices:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif 600 < mouse_x and 600 < mouse_y:
        if "9" not in choices:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif mouse_x == 300 or mouse_x == 600 or mouse_x == 900 or mouse_y == 300 or mouse_y == 600 or mouse_y == 900:
        print("Click in a square not on the edges to play")
        mouse_x, mouse_y = get_mouse_pos()
        mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
        

    return mouse_x, mouse_y