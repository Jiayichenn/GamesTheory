import random
import recursion


def check_win(current_position):
    if current_position == 0:
        return True
    else:
        return False


def check_valid_move(current_position, move):
    move = int(move)
    if move not in [1, 2]:
        return False
    if current_position - move < 0:
        return False
    return True


def start():
    print("1 for single mode, 2 for double mode")
    mode = int(input())
    if mode not in [1, 2]:
        mode = 1
    order = [0, 1]
    random.shuffle(order)
    current_position = 10
    turns = 0
    while check_win(current_position) is False:
        print("Current position is %d" % current_position)
        if order[turns] == 0:
            if mode == 1:
                print("Player please enter move")
            else:
                print("Player1 please enter move")
            move = int(input())
            while check_valid_move(current_position, move) is False:
                print("Please enter correct move")
        if order[turns] == 1:
            if mode == 2:
                print("Player2 please enter move")
                move = int(input())
                while check_valid_move(current_position, move) is False:
                    print("Please enter correct move")
            else:
                moves = recursion.best_choice(current_position)
                move = moves[0]
                print("Computer move %d" % move)
        current_position = current_position - move
        turns = (turns + 1) % 2
    turns = (turns - 1) % 2
    if order[turns] == 0:
        if mode == 1:
            print("Player win")
        else:
            print("Player1 win")
    else:
        if mode == 1:
            print("Computer win")
        else:
            print("Player2 win")


if __name__ == "__main__":
    start()
