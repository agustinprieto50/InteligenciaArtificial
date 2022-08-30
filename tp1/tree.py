from utils import Utils
from copy import deepcopy
from node import Node


OBJECTIVE = [[1,2,3],[4,5,6],[7,8,0]]
utils = Utils()

class Tree():
    def __init__(self, root):
        self.level = [root]
        pass

    def createLevel(self):
        pass

    def createTree(self):
        pass

    def createSubTree(self, node: Node):
        board = node.board
        position = utils.getPosition(board)
        possibleMoves = utils.getPossibleMoves(position)
        for i in possibleMoves:
            copyBoard = deepcopy(board)
            newBoard = utils.modifyMatrix(position, i, copyBoard)
            if node.parent == None:
                child = Node(newBoard)
                node.addChild(child)
            else: 
                if newBoard != node.parent.board:
                    child = Node(newBoard)
                    node.addChild(child)
        return node
