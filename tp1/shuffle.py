from utils import Utils


UTILS = Utils()


class Shuffle():

    def __init__(self):
        pass

    def shuffle(self, initial): 
        len(initial)
        position = UTILS.getPosition(initial)
        possibleMoves = UTILS.getPossibleMoves(position)
        newPosition = UTILS.getNewPositionRandom(possibleMoves)
        UTILS.modifyMatrix(position, newPosition, initial)
        return initial
        
    def getShuffledBoard(self, initial):
            count = 1
            while count < 20:
                self.shuffle(initial)
                count += 1
            return initial