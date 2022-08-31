from copy import copy, deepcopy
import time
from utils import Utils
from node import Node
from tree import Tree
from shuffle import Shuffle

inicio = time.time()

utils = Utils()
shuffle = Shuffle()

class TreeBidir(Tree):
    def createLevel(self):
        copyOfLevel = self.level
        self.level = []
        for node in copyOfLevel:
            children = self.createSubTree(node).children
            for i in children:
                self.level.append(i)


def createTree(treeInitial: TreeBidir, treeObjective: TreeBidir):
    while True:  
        treeInitial.createLevel()
        for i in treeInitial.level:
            for j in treeObjective.level:
                if i.board == j.board:
                    pathFromiToRoot = utils.backToRoot(i)
                    pathFromjToRoot = utils.backToRoot(j)
                    return utils.backToObjFromInitial(pathFromjToRoot, pathFromiToRoot)
        treeObjective.createLevel()
        for i in treeInitial.level:
            for j in treeObjective.level:
                if i.board == j.board:
                    pathFromiToRoot = utils.backToRoot(i)
                    pathFromjToRoot = utils.backToRoot(j)
                    return utils.backToObjFromInitial(pathFromjToRoot, pathFromiToRoot)


shuffledBoard = shuffle.getShuffledBoard([[1,2,3],[4,5,6],[7,8,0]])
initial = Node(shuffledBoard)
objective = Node([[1,2,3],[4,5,6],[7,8,0]])
treeInitial = TreeBidir(initial)
treeObjective = TreeBidir(objective)

utils.printSolutions(createTree(treeInitial, treeObjective))  
fin = time.time() - inicio
print(f'El programa tardó {fin} segundos en encontrar la solucion')      