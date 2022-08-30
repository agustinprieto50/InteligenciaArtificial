from copy import copy, deepcopy
import time
from utils import Utils
from node import Node
from tree import Tree

inicio = time.time()

utils = Utils()

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

# Objective es el arbol con el el board objetivo
# Root es el arbol con el board inicial desordenado

initial = Node([[1, 2, 3],[4, 8, 5],[7, 6, 0]])
objective = Node([[1,2,3],[4,5,6],[7,8,0]])
treeInitial = TreeBidir(initial)
treeObjective = TreeBidir(objective)

utils.printSolutions(createTree(treeInitial, treeObjective))  
fin = time.time() - inicio
print(f'El programa tardó {fin} segundos en encontrar la solucion')      