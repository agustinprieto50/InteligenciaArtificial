from copy import deepcopy
from utils import Utils


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
    def __init__(self, root, objective):
        self.rootLevels = [[[root]]]
        self.objectiveLevels = [[[objective]]]
        pass

    def createRootLevel(self):
        for level in self.rootLevels:
            auxLevel = []
            for sublevel in level:
                for node in sublevel:
                    auxSubLeveL = []
                    board = node.board
                    position = utils.getPosition(board)
                    possibleMoves = utils.getPossibleMoves(position)
                    for i in possibleMoves:
                        copyBoard = deepcopy(board)
                        newBoard = utils.modifyMatrix(position, i, copyBoard)
                        child = Node(newBoard)
                        node.addChild(child)
                        auxSubLeveL.append(child)
                    auxLevel.append(auxSubLeveL)
            
        self.rootLevels.append(auxLevel)

    def createObjLevel(self):
        for level in self.objectiveLevels:
            auxLevel = []
            for sublevel in level:
                for node in sublevel:
                    auxSubLeveL = []
                    board = node.board
                    position = utils.getPosition(board)
                    possibleMoves = utils.getPossibleMoves(position)
                    for i in possibleMoves:
                        copyBoard = deepcopy(board)
                        newBoard = utils.modifyMatrix(position, i, copyBoard)
                        child = Node(newBoard)
                        node.addChild(child)
                        auxSubLeveL.append(child)
                    auxLevel.append(auxSubLeveL)
            
        self.objectiveLevels.append(auxLevel)


    def createBirDirTree(self):
        while True:
            self.createRootLevel()
            self.createObjLevel()
            for rootLvl in self.rootLevels:
                for objLvl in self.objectiveLevels:
                    for rootSubLvl in rootLvl:
                        for objSubLvl in objLvl:
                            for rootNode in rootSubLvl:
                                for objNode in objSubLvl:
                                    if rootNode.board == objNode.board:
                                        return [objNode, rootNode]

    


    

# Objective es el arbol con el el board objetivo
# Root es el arbol con el board inicial desordenado

root = Node([[1, 0, 3], [4, 2, 6], [7, 5, 8]])
objective = Node([[1,2,3],[4,5,6],[7,8,0]])

tree = Tree(root, objective)
intersectionObj, intersectionRoot = tree.createBirDirTree()
pathToRoot = utils.backToRoot(intersectionRoot)
pathToObj = utils.backToRoot(intersectionObj)
completePath = utils.backToObjFromRoot(pathToObj, pathToRoot)
utils.printSolutions(completePath)

                

        