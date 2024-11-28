matrix = [[2, 8, 4, 2], 
         [4, 32, 8, 4], 
         [32, 64, 16, 8], 
         [2, 16, 2, 16]]

from functions import update, start, new_2, left, transpose, right, up, down, left_is_legal, right_is_legal, up_is_legal, down_is_legal, won, lost

start(matrix)

while(won(matrix) == False and lost(matrix) == False):
    print()
    key = input("keep going! ")
    print()
    if key == "a":  
        if left_is_legal(matrix):         
            left(matrix)
            new_2(matrix)
            update(matrix)
        else:
            print("try a different key!")
            print()
            update(matrix)
    elif key == "d":           
        if right_is_legal(matrix):         
            right(matrix)
            new_2(matrix)
            update(matrix)
        else:
            print("try a different key!")
            print()
            update(matrix)
    elif key == "w":           
        if up_is_legal(matrix):         
            up(matrix)
            new_2(matrix)
            update(matrix)
        else:
            print("try a different key!")
            print()
            update(matrix)
    elif key == "s":           
        if down_is_legal(matrix):         
            down(matrix)
            new_2(matrix)
            update(matrix)
        else:
            print("try a different key!")
            print()
            update(matrix)
    else:
        print("use asdw to navigate!")
        update(matrix)


if won(matrix):
    print()
    print("you are insane!")
else:
    print()
    print("you're trash!")



    
