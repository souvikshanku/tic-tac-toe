
BOARD = list("""
+-----+-----+-----+
|     |     |     |
+-----+-----+-----+
|     |     |     |
+-----+-----+-----+
|     |     |     |
+-----+-----+-----+
""")  # Since strings are immutable

POS = [24, 30, 36, 64, 70, 76, 104, 110, 116]


def draw_board(state):
    for i, move in enumerate(state):
        if move == 1:
            BOARD[POS[i]] = "X"
        elif move == 2:
            BOARD[POS[i]] = "O"

    print("".join(BOARD))
    check_game_over(state)


def check_game_over(state):
    for i in [0, 3, 6]:
        if state[i + 0] == state[i + 1] == state[i + 2] == 1:
            print("Player 1 Wins! 🎉")
            return
        elif state[i + 0] == state[i + 1] == state[i + 2] == 0:
            print("Player 2 Wins! 🎉")
            return

    for i in range(3):
        if state[i + 0] == state[i + 3] == state[i + 6] == 1:
            print("Player 1 Wins! 🎉")
            return
        if state[i + 0] == state[i + 3] == state[i + 6] == 0:
            print("Player 2 Wins! 🎉")
            return
    
    if state[0] == state[4] == state[8]:
        if state[0] == 1:
            print("Player 1 Wins! 🎉")
        else:
            print("Player 2 Wins! 🎉")

    elif state[2] == state[4] == state[6]:
        if state[0] == 1:
            print("Player 1 Wins! 🎉")
        else:
            print("Player 2 Wins! 🎉")



if __name__ == "__main__":
    state = [2, 0, 2, 0, 2, 2, 1, 1, 2]
    draw_board(state)
