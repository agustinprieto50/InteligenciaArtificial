from shuffle import Shuffle
from randomSolution import randomSolution


SHUFFLE = Shuffle()

initial = [[1,2,3],[4,5,6],[7,8,0]]

# SHUFFLE
new_board = SHUFFLE.getShuffledBoard(initial)
print(f"\nTablero despues de 20 movimientos: {new_board}")


# RANDOM SOLUTION
solved_board = randomSolution(new_board)
print(solved_board)


