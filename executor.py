matrix = [[0, 0, 0, 0], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0]]

from functions import update, start, new_2, havent_won_yet, left, right, transpose, up, down, havent_lost_yet 

start(matrix)

while(havent_won_yet and havent_lost_yet):
    key = input("keep going! ")
    if key == "a":           
        left(matrix)
        new_2(matrix)
        update(matrix)
    if key == "d":           
        right(matrix)
        new_2(matrix)
        update(matrix)
    if key == "w":           
        up(matrix)
        new_2(matrix)
        update(matrix)
    if key == "s":           
        down(matrix)
        new_2(matrix)
        update(matrix)    

if havent_won_yet == False:
    print("you are insane!")
else:
    print("you fucking suck!")



    
