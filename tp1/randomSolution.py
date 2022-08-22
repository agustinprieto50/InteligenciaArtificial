from shuffle import Shuffle


SHUFFLE = Shuffle()

def randomSolution(board):
    OBJECTIVE = [[1,2,3],[4,5,6],[7,8,0]]
    count = 1
    while True:
        new_board = SHUFFLE.shuffle(board)
        count += 1

        if new_board == OBJECTIVE:
            return f"\nThe program needed {count} moves to solve the problem. Board: {new_board}\n"
