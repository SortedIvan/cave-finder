from tkinter import *
import queue
from turtle import bgcolor
import numpy as np
import random as random
from cavegen import GenerateRandomMap,CountNeighbours, SmoothenMap
# 1) A map of a 2D array must be generated with initial random cells (given a number)
# 2) A function that counts how many neighbours a cell has
# 3) Rulesets for how a cell lives or dies


 
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
                    self.e = Entry(root, width=3, bg='red',
                               font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j)

                elif str(self.e.get()) == "0":
                    self.e = Entry(root, width=3, bg='blue',
                               font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j)




# MAIN ALGORITHM

nums = queue.Queue()
nums.put("")
add = ""
# -------------- MAP GENERATION -----------------------------
cave = GenerateRandomMap()
for i in range(3):
    cave = SmoothenMap(cave)

#------------------------------------------------------------


lst = cave

total_rows = len(lst)
total_columns = len(lst[0])

# create root window
root = Tk()
t = Table(root)
root.mainloop()
