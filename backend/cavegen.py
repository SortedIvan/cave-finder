import numpy as np
import random as random
# 1) A map of a 2D array must be generated with initial random cells (given a number)
# 2) A function that counts how many neighbours a cell has
# 3) Rulesets for how a cell lives or dies
chance = 0.45
deathLimit = 3
birthLimit = 4
randomNr = random.uniform(0, 1)

def RandomNrGen():
    randomNr = random.uniform(0, 1)
    return round(randomNr, 2)

def GenerateRandomMap():
    matrix = np.zeros([25, 25], dtype=int)
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for x in range(0, rows):
        for y in range(0, cols):
            if (x == 0 or x == rows - 1 or y == 0 or y == cols - 1): # Ensure that the outer cells are walls
                matrix[x,y] = 1
            else:
                if (chance > RandomNrGen()):
                    matrix[x,y] = 1
    return matrix

def CountNeighbours(map, cellx, celly):
    count = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            neighbour_x = cellx + i
            neighbour_y = celly + j
            if (i == 0 and j == 0):
                print("")
            elif(neighbour_x < 0 or neighbour_y < 0 or neighbour_x >= len(map) or neighbour_y >= len(map[0])):
                count = count + 1
            elif (map[neighbour_x, neighbour_y]):
                count = count + 1
    return count


def SmoothenMap(map):
    oldMap = map
    rows = oldMap.shape[0]
    cols = oldMap.shape[1]
    newMap = np.zeros([5,5], dtype=int) # Make a new map with the same size as before
    for x in range(0, rows):
        for y in range(0, cols):
            N = CountNeighbours(oldMap,x,y)
            if (oldMap[x,y] == 1):
                if (N < deathLimit):
                    newMap[x,y] = 0
                newMap[x,y] = 1
            else:
                if(N > birthLimit):
                    newMap[x,y] = 1
                else:
                    newMap[x,y] = 0
    return newMap

                




GenerateRandomMap()
print(round(randomNr, 2))