import numpy as np
import random as random
from PIL import Image
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


# Generating a random map based on the input of a user
def GenerateRandomMap():
    matrix = np.zeros([ 50,50], dtype=int)
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


# Function to count all of the neighbors that a map has
def CountNeighbours(map, cellx, celly):
    count = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            neighbour_x = cellx + i
            neighbour_y = celly + j
            if (i == 0 and j == 0):
                pass
            elif(neighbour_x < 0 or neighbour_y < 0 or neighbour_x >= len(map) or neighbour_y >= len(map[0])):
                count = count + 1
                pass
            elif (map[neighbour_x, neighbour_y]):
                count = count + 1
    return count

# Smoothening function, applying cellular automata rules
def SmoothenMap(map):
    oldMap = map
    rows = oldMap.shape[0]
    cols = oldMap.shape[1]
    newMap = np.zeros([50,50], dtype=int) # Make a new map with the same size as before
    for x in range(0, rows):
        for y in range(0, cols):
            N = count_neighbours(x,y, oldMap)
            if (oldMap[x,y] == 1):
                if (N < 4):
                    newMap[x,y] = 0
                newMap[x,y] = 1
            else:
                if(N > 4):
                    newMap[x,y] = 1
                else:
                    newMap[x,y] = 0
    return newMap


def count_neighbours(a, b, map):
    neighbours = 0
    for i in (a-1, a, a+1):
        for j in (b-1, b, b+1):
            if i != a or j != b: # we do not need to count the square itself whose neighbours we're counting
                if i in range(0, 25) and j in range(0, 25): # to check if the square is within bounds
                    if map[i,j]: #neighbour at i, j located
                        neighbours += map[i,j]
    return neighbours



map = GenerateRandomMap()
for i in range(5):
    map = SmoothenMap(map)
    print(map)
    print("-------------------------------------------------------------------------------------------" + '\n')

img = Image.new('1', (50, 50))
pixels = img.load()

for i in range(img.size[0]):
   for j in range(img.size[1]):
        pixels[i, j] = int(map[i,j])

img.show()
img.save('cave.bmp')