import random



class Utils():

    def __init__(self):
        pass

    def getPossibleMoves(self, position):
        row = position[0]
        column = position[1]
        possible_moves = []

        if row + 1 < 3:
            new = [row + 1, column]
            possible_moves.append(new) 
        if row - 1 >= 0:
            new = [row - 1, column]
            possible_moves.append(new) 
        if column + 1 < 3:
            new = [row, column+1]
            possible_moves.append(new) 
        if column - 1 >= 0:
            new = [row, column-1]
            possible_moves.append(new) 
        return possible_moves

    def getPosition(self, initial):
        for i in range(len(initial)):
            for j in range(len(initial[i])):
                if initial[i][j] == 0:
                    position = [i, j]
        return position

    def getNewPositionRandom(self, possibleMoves):
        moves_count = len(possibleMoves)-1
        new_position = possibleMoves[random.randint(0, moves_count)]
        return new_position

    def modifyMatrix(self, position, newPosition, initial):
        initial[position[0]][position[1]] = initial[newPosition[0]][newPosition[1]]
        initial[newPosition[0]][newPosition[1]] = 0
        return initial

    def getParent(self, node):
        try:
            return node.parent
        except None:
            return False

    # Objective es el nodo final
    def backToRoot(self, objective):
        nodes = [objective]
        for i in nodes:
            parent = self.getParent(i)
            if parent:
                nodes.append(parent)
        return nodes

    def backToObjFromRoot(self, pathToObj, pathToRoot):
        pathToObjFromRoot = []
        for i in reversed(pathToObj):
            pathToObjFromRoot.append(i)
        for j in pathToRoot:
            pathToObjFromRoot.append(j)
        return pathToObjFromRoot



    def printSolutions(self, solutions: list):
        for node in reversed(solutions):
            for row in node.board:
                print(row)
            print('\n')


