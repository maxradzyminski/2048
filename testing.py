matrix = [[2, 2, 2, 2], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0]]

from functions import update, spawn, start, new_2, havent_won_yet, left, right, transpose, up, down

start(matrix)
while(havent_won_yet):
    key = input("keep going! ")
    if key == "s":           
        down(matrix)
        new_2(matrix)
        update(matrix)


