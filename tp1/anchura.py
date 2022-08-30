from utils import Utils
from shuffle import Shuffle
from tree import Tree

OBJECTIVE = [[1,2,3],[4,5,6],[7,8,0]]
    
    
class TreeAnchura(Tree):

    def createLevel(self):
        copyOfLevel = self.level
        self.level = []
        for node in copyOfLevel:
            if node.board == OBJECTIVE:
                return node
            children = self.createSubTree(node).children
            for i in children:
                self.level.append(i)


    def createTree(self):
        while True:
            tree = self.createLevel()
            if tree:
                print("\nEl programa encontró la solucion!", '\n')
                return tree

