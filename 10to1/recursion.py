def generate_moves(position):
    if position >= 2:
        return [1, 2]
    elif position == 1:
        return [1]
    else:
        return []


def do_move(current_position, move):
    return current_position - move


def primitive(current_position):
    if current_position == 0:
        return "L"
    elif ((current_position - 1 == 0) or (current_position - 2 == 0)):
        return "W"
    else:
        results = [primitive(current_position - next_move)
                   for next_move in generate_moves(current_position)]
        if "L" in results:
            return "W"
        return "L"


def best_choice(current_position):
    if current_position >= 2:
        results = [primitive(current_position - next_move)
                   for next_move in generate_moves(current_position)]
        if results[0] == "L":
            return [1]
        elif results[1] == "L":
            return [2]
        else:
            return [1, 2]
    else:
        return [1]


def solve(p):
    print(primitive(p))


if __name__ == "__main__":
    for i in range(10, -1, -1):
        solve(i)
