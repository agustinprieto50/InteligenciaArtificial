from shuffle import Shuffle
import time
from utils import Utils
from node import Node
from anchura import TreeAnchura

def main():
    OBJECTIVE = [[1,2,3],[4,5,6],[7,8,0]]
    shuffle = Shuffle()
    utils = Utils()
    inicio = time.time()
    shuffledBoard = shuffle.getShuffledBoard(OBJECTIVE)
    print(f'Board inicial: {shuffledBoard}')
    root = Node(shuffledBoard)
    tree = TreeAnchura(root)
    solutionNode = tree.createTree()
    solutionArray = utils.backToRoot(solutionNode)
    utils.printSolutions(solutionArray)
    fin = time.time() - inicio
    print(f'El programa tardó {fin} segundos en encontrar la solución\n')

if __name__ == '__main__':
    main()
