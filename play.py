import os
import random

from board import draw_board, evaluate
from minimax import Node, minimax


def make_move(move, state, as_player):
    board_pos = {
        "a1": 6, "a2": 3, "a3": 0,
        "b1": 7, "b2": 4, "b3": 1,
        "c1": 8, "c2": 5, "c3": 2,
    }

    idx = board_pos[move]
    state[idx] = as_player
    return state


def choose_move(state, as_player):
    node = Node(state)

    if as_player == 1:
        value = minimax(node, depth=9, maximize=False)
        node.expand(player=2)
        for child in node.children:
            if value == minimax(Node(child.state), depth=9, maximize=True):
                return child.state
    else:
        value = minimax(node, depth=9, maximize=True)
        node.expand(player=1)
        for child in node.children:
            if value == minimax(Node(child.state), depth=9, maximize=False):
                return child.state


def render(state):
    os.system("clear")
    draw_board(state)


if __name__ == "__main__":
    player = input("You wanna go first? - 1 (yes). 2 (no)\n")
    os.system("clear")

    if player == "1":
        state = [0] * 9
        draw_board(state)
        while not (Node(state).is_game_over()):
            move = input("Your move? ")
            state = make_move(move, state, as_player=1)
            state = choose_move(state, as_player=1)
            render(state)

    else:
        move = random.choice(range(9))
        state = [0] * 9
        state[move] = 1
        draw_board(state)

        while not (Node(state).is_game_over()):
            move = input("Your move? ")
            state = make_move(move, state, as_player=2)
            state = choose_move(state, as_player=2)
            render(state)

    value = evaluate(state)

    if value == 1:
        print("Player 1 Wins!")
    elif value == -1:
        print("Player 2 Wins!")
    else:
        print("It's a draw!")
