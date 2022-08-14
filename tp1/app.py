from shuffle import getShuffledBoard
from randomSolution import randomSolution

initial = [[1,2,3],[4,5,6],[7,8,0]]
new_board = getShuffledBoard(initial)
solved_board = randomSolution(new_board)
print(solved_board)

