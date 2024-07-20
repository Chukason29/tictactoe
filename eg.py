game_boxes = [
        ["O", "O", "O"],
        ["O", "O", "O"],
        ["O", "O", "O"],
    ]
def is_game_finished():
    check = False
    for x in game_boxes:
        if x[0] != "O" or x[1] !="O" or x[2] != "O":
            check = True
    return check
print(is_game_finished())