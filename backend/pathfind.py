import queue
from tkinter import *

def createCave():
    cave = []
    cave.append(["#","#", "#", "#", "#", "O","#"])
    cave.append(["#"," ", " ", " ", "#", " ","#"])
    cave.append(["#"," ", "#", " ", "#", " ","#"])
    cave.append(["#"," ", "#", " ", " ", " ","#"])
    cave.append(["#"," ", "#", "#", "#", " ","#"])
    cave.append(["#"," ", " ", "X", "#", " ","#"])
    cave.append(["#","#", "#", "#", "#", "#","#"])

    return cave

def createCave2():
    cave = []
    cave.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    cave.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    cave.append(["#"," ", "#", "#", "#", "#", "#", " ", "#"])
    cave.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    cave.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    cave.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    cave.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    cave.append(["#"," ", " ", " ", " ", " ", " ", "X", "#"])
    cave.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])

    return cave


def printCave(cave, path=""):
    for x, pos in enumerate(cave[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(cave):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(cave, moves):
    for x, pos in enumerate(cave[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(cave[0]) and 0 <= j < len(cave)):
            return False
        elif (cave[j][i] == "#"):
            return False

    return True


def findEnd(cave, moves):
    for x, pos in enumerate(cave[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if cave[j][i] == "X":
        print("Found: " + moves)
        printCave(cave, moves)
        return True

    return False


# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
cave  = createCave2()

while not findEnd(cave, add): 
    add = nums.get()
    #print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(cave, put):
            nums.put(put)
