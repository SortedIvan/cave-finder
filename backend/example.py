from tkinter import *
import queue
from turtle import bgcolor

# def createCave():
#     cave = []
#     cave.append(["#","#", "#", "#", "#", "O","#"])
#     cave.append(["#"," ", " ", " ", "#", " ","#"])
#     cave.append(["#"," ", "#", " ", "#", " ","#"])
#     cave.append(["#"," ", "#", " ", " ", " ","#"])
#     cave.append(["#"," ", "#", "#", "#", " ","#"])
#     cave.append(["#"," ", " ", "X", "#", " ","#"])
#     cave.append(["#","#", "#", "#", "#", "#","#"])
#     return cave

# def createCave2():
#     cave = []
#     cave.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
#     cave.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
#     cave.append(["#"," ", "#", "#", "#", "#", "#", " ", "#"])
#     cave.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
#     cave.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
#     cave.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
#     cave.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
#     cave.append(["#"," ", " ", " ", " ", " ", " ", "X", "#"])
#     cave.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])
#     return cave


# def printCave(cave, path=""):
#     for x, pos in enumerate(cave[0]):
#         if pos == "O":
#             start = x

#     i = start
#     j = 0
#     pos = set()
#     for move in path:
#         if move == "L":
#             i -= 1

#         elif move == "R":
#             i += 1

#         elif move == "U":
#             j -= 1

#         elif move == "D":
#             j += 1
#         pos.add((j, i))
    
#     for j, row in enumerate(cave):
#         for i, col in enumerate(row):
#             if (j, i) in pos:
#                 print("+ ", end="")
#             else:
#                 print(col + " ", end="")
#         print()
        


# def valid(cave, moves):
#     for x, pos in enumerate(cave[0]):
#         if pos == "O":
#             start = x

#     i = start
#     j = 0
#     for move in moves:
#         if move == "L":
#             i -= 1

#         elif move == "R":
#             i += 1

#         elif move == "U":
#             j -= 1

#         elif move == "D":
#             j += 1

#         if not(0 <= i < len(cave[0]) and 0 <= j < len(cave)):
#             return False
#         elif (cave[j][i] == "#"):
#             return False

#     return True


# def findEnd(cave, moves):
#     for x, pos in enumerate(cave[0]):
#         if pos == "O":
#             start = x

#     i = start
#     j = 0
#     for move in moves:
#         if move == "L":
#             i -= 1

#         elif move == "R":
#             i += 1

#         elif move == "U":
#             j -= 1

#         elif move == "D":
#             j += 1

#     if cave[j][i] == "X":
#         print("Found: " + moves)
#         printCave(cave, moves)
#         return True

#     return False

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
    matrix = np.zeros([25, 25], dtype=int)
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

 
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                
                self.e = Entry(root, width=3, fg='blue',
                               font=('Arial',16,'bold'))
                 

                
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

                if str(self.e.get()) == "1":
                    # print("Yessir")
                    self.e = Entry(root, width=3, bg='red',
                               font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j)
                    # self.e.insert(END, lst[i][j])

                elif str(self.e.get()) == "0":
                    # print("Nosir")
                    self.e = Entry(root, width=3, bg='blue',
                               font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j)
                    # self.e.insert(END, lst[i][j])

                



                # print("This is self E " + str(self.e.get()) + "!")



# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
cave  = GenerateRandomMap()

# while not findEnd(cave, add): 
#     add = nums.get()
#     #print(add)
#     for j in ["L", "R", "U", "D"]:
#         put = add + j
#         if valid(cave, put):
#             nums.put(put)

lst = cave

total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()
