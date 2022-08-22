from copy import deepcopy
from utils import Utils

OBJECTIVE = [[1,2,3],[4,5,6],[7,8,0]]

utils = Utils()

class Node():
    def __init__(self, board):
        self.board = board
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)
    
    
class Tree():
    def __init__(self, root):
        self.levels = [[[root]]]
        pass

    def createLevel(self):
        for level in self.levels:
                auxLevel = []
                for sublevel in level:
                    for node in sublevel:
                        auxSubLeveL = []
                        board = node.board
                        if board == OBJECTIVE:
                            print("The program found the solution!", board)
                            return node
                        position = utils.getPosition(board)
                        possibleMoves = utils.getPossibleMoves(position)
                        for i in possibleMoves:
                            copyBoard = deepcopy(board)

                            newBoard = utils.modifyMatrix(position, i, copyBoard)

                            child = Node(newBoard)
                            node.addChild(child)
                            auxSubLeveL.append(child)
                        auxLevel.append(auxSubLeveL)

                
                self.levels.append(auxLevel)

    def createTree(self):
        while True:
            tree = self.createLevel()
            if tree:
                return tree


root = Node([[1, 0, 3], [4, 2, 6], [7, 5, 8]])
tree = Tree(root)
solutionNode = tree.createTree()
solutionArray = utils.objectiveToInitial(solutionNode)
utils.printSolutions(solutionArray)

