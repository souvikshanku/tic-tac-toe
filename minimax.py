from board import evaluate, draw_board


class Node:
    def __init__(self, game_state):
        self.state = game_state
        self.children = []
        self.value = - 1e4

    def __repr__(self):
        return str(self.state)

    def expand(self, player):
        for i, cell in enumerate(self.state):
            if cell == 0:
                new_state = self.state.copy()
                new_state[i] = player
                self.children.append(Node(new_state))

        return self.children

    def is_game_over(self):
        value = evaluate(self.state)
        if value is None:
            return False
        return True


def minimax(node, depth, maximize):
    if depth == 0 or node.is_game_over():
        return evaluate(node.state)

    children = node.expand(1 if maximize else 2)

    if maximize:
        max_value = -1e4
        for child in children:
            value = minimax(child, depth - 1, False)
            max_value = max(max_value, value)

        return max_value

    else:
        min_value = 1e4
        for child in children:
            value = minimax(child, depth - 1, True)
            min_value = min(min_value, value)

        return min_value


node = Node([1, 0, 2, 0, 1, 0, 0, 0, 0])
node.expand(2)
draw_board(node.state)

for child in node.children:
    draw_board(child.state)
    value = minimax(child, depth=9, maximize=True)
    print(value)
