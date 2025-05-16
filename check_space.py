
from get_mouse import get_mouse_pos

def check_space(mouse_x, mouse_y, choices):#checks the space the user chose and if it is taken the user needs to choose a different one 
    if mouse_x < 300 and mouse_y < 300:
        if choices["1"]:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif 300 < mouse_x < 600 and mouse_y < 300:
        if choices["2"]:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif 600 < mouse_x and mouse_y < 300:
        if choices["3"]:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif mouse_x < 300 and 300 < mouse_y < 600:
        if choices["4"]:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif 300 < mouse_x < 600 and 300 < mouse_y < 600:
        if choices["5"]:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif 600 < mouse_x and 300 < mouse_y < 600:
        if choices["6"]:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif mouse_x < 300 and 600 < mouse_y:
        if choices["7"]:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif 300 < mouse_x < 600 and 600 < mouse_y:
        if choices["8"]:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif 600 < mouse_x and 600 < mouse_y:
        if choices["9"]:
            print("Already Taken. Try Again!")
            mouse_x, mouse_y = get_mouse_pos()
            mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
    elif mouse_x == 300 or mouse_x == 600 or mouse_x == 900 or mouse_y == 300 or mouse_y == 600 or mouse_y == 900:
        print("Click in a square not on the edges to play")
        mouse_x, mouse_y = get_mouse_pos()
        mouse_x, mouse_y = check_space(mouse_x, mouse_y, choices)
        

    return mouse_x, mouse_y