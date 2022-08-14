from shuffle import shuffle


def randomSolution(board):
    count = 1
    while True:
        new_board = shuffle(board)
        count += 1

        if new_board == [[1,2,3],[4,5,6],[7,8,0]]:
            return f"The program needed {count} moves to solve the problem. Board: {new_board}"