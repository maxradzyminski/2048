import random

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

def havent_won_yet(matrix):
    for row in matrix:
        for element in row:
            if element == 2048:
                return False
            else:
                return True

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
        for i in range(1,5):
            if i < 4:
                if row[-i] == row[-i - 1]:
                    row[-i] = row[-i] * 2
                    row[-i-1] = 0 
    left_squish(matrix)


def right_squish(matrix):
    for row in matrix:
        list = [0, 0, 0, 0]
        counter = -1
        for i in range(1,5):
            if row[-i] != 0:
                list[counter] = row[-i]
                counter = counter - 1
        matrix[matrix.index(row)] = list

def right(matrix): 
    right_squish(matrix)
    for row in matrix:
        for i in range(0,4):
            if i  > 0:
                if row[i] == row[i - 1]:
                    row[i] = row[i] * 2
                    row[i-1] = 0 
    right_squish(matrix)

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

def up(matrix):
    transpose(matrix)
    left(matrix)
    transpose(matrix)
    transpose(matrix)
    transpose(matrix)

def down(matrix):
    transpose(matrix)
    right(matrix)
    transpose(matrix)
    transpose(matrix)
    transpose(matrix)

def havent_lost_yet(matrix):
    list = []
    for i in range(0,4):
        for j in range(0,4):
            if matrix[i][j] == 0:
                list.append([i,j])
    if len(list) == 0:
        return False
    else:
        return True

