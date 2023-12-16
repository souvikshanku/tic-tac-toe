class Node:
    def __init__(self, game_state, parent):
        self.state = game_state
        self.parent = parent
        self.children = []

    def __repr__(self):
        return str(self.state)

    def expand(self, player):
        for i, cell in enumerate(self.state):
            if cell == 0:
                new_state = self.state.copy()
                new_state[i] = player
                self.children.append(Node(new_state, self))


node = Node([1, 2, 0, 0], None)
node.expand(1)

print(node.children)
