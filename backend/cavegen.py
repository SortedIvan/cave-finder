from tkinter import Widget
from turtle import width
import numpy as np
import random as random
# 1) A map of a 2D array must be generated with initial random cells (given a number)
# 2) A function that counts how many neighbours a cell has
# 3) Rulesets for how a cell lives or dies
chance = 0.45
randomNr = random.uniform(0, 1)

def RandomNrGen():
    randomNr = random.uniform(0, 1)
    return round(randomNr, 2)



def GenerateRandomMap():
    matrix = np.zeros([5, 5], dtype=int)
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    matrix[4,3] = 1
    for x in range(0, rows):
        for y in range(0, cols):
            if (x == 0 or x == rows - 1 or y == 0 or y == cols - 1):
                matrix[x,y] = 1
            else:
                if (chance > RandomNrGen()):
                    matrix[x,y] = 1
    return matrix

print(GenerateRandomMap())
print(round(randomNr, 2))