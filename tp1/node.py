
class Node():
    def __init__(self, board):
        self.board = board
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)
