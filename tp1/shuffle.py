from hashlib import new
from operator import truediv
import random
from traceback import print_tb
from turtle import pos, position
from webbrowser import get

# initial = [[1,2,3],[4,5,6],[7,8,0]]
initial = [[1, 2, 3], [7, 4, 5], [0, 8, 6]]


def getPossibleMoves(position: list):
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


def getPosition(initial):
    for i in range(len(initial)):
        for j in range(len(initial[i])):
            if initial[i][j] == 0:
                position = [i, j]
    return position

def getNewPosition(possibleMoves):
    moves_count = len(possibleMoves)-1
    new_position = possibleMoves[random.randint(0, moves_count)]
    return new_position

def modifyMatrix(position, newPosition, initial):
    initial[position[0]][position[1]] = initial[newPosition[0]][newPosition[1]]
    initial[newPosition[0]][newPosition[1]] = 0
    return initial


def shuffle(initial): 
    position = getPosition(initial)
    possibleMoves = getPossibleMoves(position)
    newPosition = getNewPosition(possibleMoves)
    modifyMatrix(position, newPosition, initial)
    return initial
    

def getShuffledBoard(initial):
        count = 1
        while count < 20:
            shuffle(initial)
            count += 1
        print(initial, count)
        return initial