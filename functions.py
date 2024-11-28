import random
import copy

def update(matrix):
    for row in matrix:
        for element in row:
            print(element, end="  ")
        print()

def spawn(matrix):
    first_index = random.randint(0,3), random.randint(0,3)
    second_index = random.randint(0,3), random.randint(0,3)
    different_check = True
    while different_check:
        if first_index == second_index:
            second_index = random.randint(0,3), random.randint(0,3)
        else:
            different_check = False
            matrix[first_index[0]][first_index[1]] = 2
            matrix[second_index[0]][second_index[1]] = 2

def start(matrix): 
    print("""
2048!
Use aswd and enter to play.
          """)
    spawn(matrix)
    update(matrix)

def new_2(matrix):
    list = []
    for i in range(0,4):
        for j in range(0,4):
            if matrix[i][j] == 0:
                list.append([i,j])
    index = random.randint(0, len(list)-1)
    row = list[index][0]
    column = list[index][1]
    matrix[row][column] = 2

def left_squish(matrix):
    for row in matrix:
        list = [0, 0, 0, 0]
        counter = 0
        for element in row:
            if element != 0:
                list[counter] = element
                counter = counter + 1
        matrix[matrix.index(row)] = list

def left(matrix): 
    left_squish(matrix)
    for row in matrix:
        for i in range(0,4):
            if i < 3:
                if row[i] == row[i + 1]:
                    row[i] = row[i] * 2
                    row[i+1] = 0 
    left_squish(matrix)

def transpose(matrix):
    row_one = []
    row_two = []
    row_three = []
    row_four = []
    for row in matrix:
        row_one.append(row[0])
        row_two.append(row[1])
        row_three.append(row[2])
        row_four.append(row[3])
    matrix[0] = row_one 
    matrix[1] = row_two
    matrix[2] = row_three
    matrix[3] = row_four

def reverse(matrix):
    for row in matrix:
        row.reverse()

def right(matrix):
    reverse(matrix)
    left(matrix)
    reverse(matrix)

def up(matrix):
    transpose(matrix)
    left(matrix)
    transpose(matrix)
    transpose(matrix)
    transpose(matrix)

def down(matrix):
    transpose(matrix)
    reverse(matrix)
    left(matrix)
    reverse(matrix)
    transpose(matrix)

def left_is_legal(matrix):
    new = copy.deepcopy(matrix)
    left(new)
    if matrix != new:
        return True
    else:
        return False

def right_is_legal(matrix):
    new = copy.deepcopy(matrix)
    right(new)
    if matrix != new:
        return True
    else:
        return False

def up_is_legal(matrix):
    new = copy.deepcopy(matrix)
    up(new)
    if matrix != new:
        return True
    else:
        return False

def down_is_legal(matrix):
    new = copy.deepcopy(matrix)
    down(new)
    if matrix != new:
        return True
    else:
        return False
    
def won(matrix):
    for row in matrix:
        for element in row:
            if element == 2048:
                return True
    return False
            
def lost(matrix):
    if (left_is_legal(matrix) == False and right_is_legal(matrix) == False and up_is_legal(matrix) == False and 
    down_is_legal(matrix) == False):
        return True
    else:
        return False
        