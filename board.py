BOARD = list("""
    +-----+-----+-----+
 3  |     |     |     |
    +-----+-----+-----+
 2  |     |     |     |
    +-----+-----+-----+
 1  |     |     |     |
    +-----+-----+-----+
       a     b     c
""")  # Since strings are immutable


def draw_board(state):
    board = BOARD.copy()

    pos = [32, 38, 44, 80, 86, 92, 128, 134, 140]

    for i, move in enumerate(state):
        if move == 1:
            board[pos[i]] = "X"
        elif move == 2:
            board[pos[i]] = "O"

    print("".join(board))


def evaluate(state):
    for i in [0, 3, 6]:
        if state[i + 0] == state[i + 1] == state[i + 2] == 1:
            return 1
        elif state[i + 0] == state[i + 1] == state[i + 2] == 2:
            return -1

    for i in range(3):
        if state[i + 0] == state[i + 3] == state[i + 6] == 1:
            return 1
        if state[i + 0] == state[i + 3] == state[i + 6] == 2:
            return -1

    if state[0] == state[4] == state[8] == 1:
        return 1
    if state[0] == state[4] == state[8] == 2:
        return -1

    if state[2] == state[4] == state[6] == 1:
        return 1
    if state[2] == state[4] == state[6] == 2:
        return -1

    # Draw
    if 0 not in state:
        return 0

    else:
        return None


if __name__ == "__main__":
    state = [2, 0, 2, 0, 2, 2, 1, 1, 2]
    draw_board(state)
