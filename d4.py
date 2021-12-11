import numpy as np

def get_matrix(file_lines):
    orignal_matrix = []
    matrix = [] 
    for line in file_lines:
        if line == "\n":
            orignal_matrix.append(matrix)
            matrix = [] 
        else:
            line = list(map(int, 
                   line.strip().split()))
            matrix.append(line)
    orignal_matrix.append(matrix)
    return orignal_matrix

def del_and_X(rows, num):
    if num in rows:
        position = rows.index(num)
        del rows[position]
        rows.insert(position, "X")
    return rows

def prt_matrix(matrix):
    for row in matrix:
        print(row)
    print("-"*10)

def rmv_num(matrix, num):
    for row in matrix:
        del_and_X(row, num)
    prt_matrix(matrix)
    return matrix

def transpose(x):
    return [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

def check_if_bingo(matrix):
    for winning_line,row in enumerate(matrix):
        if row == ["X","X","X","X","X"]:
            return (True,winning_line)

    return (False,None)

def check_rows(matrix):
    bingo, winning_line = check_if_bingo(matrix)
    if bingo:
        return (True, winning_line, "row")
    else:
        return (False, None, None)


def check_colums(matrix):
    matrix_t =  transpose(matrix)
    bingo, winning_line = check_if_bingo(matrix_t)
    matrix =  transpose(matrix_t)
    if bingo:
        return (True, winning_line, "colum")
    else:
        return (False, None, None)

def sum_unused(matrix):
    sum = 0
    for row in matrix:
        for elem in row:
            if elem != "X":
                sum = sum + elem
    return sum

def bingo_combo(matrix_orig, matrix_bingo, result, last_num):
    bingo, win_row, row_col = result
    if bingo:
        if row_col == "row":
            print(matrix_orig[win_row])
            prt_matrix(matrix_bingo)
            sum_num =sum_unused(matrix_bingo)
            print(sum_num,"*",last_num,"=",sum_num*last_num)
            return True
        elif row_col == "colum":
            matrix_orig_t =  transpose(matrix_orig)
            print(matrix_orig_t[win_row])
            sum_num =sum_unused(matrix_bingo)
            print(sum_num,"*",last_num,"=",sum_num*last_num)
            return True
        else:
            return False


file = open("bingo_0.txt", "r")
lines = file.readlines()

bingo_numbers = list(map(int, lines[0].strip().split(",")))

all =  get_matrix(lines[2:])
orig = get_matrix(lines[2:])

for num in bingo_numbers: 
    for mtx_n, matrix0 in enumerate(all):
        print("mtx:", mtx_n)
        matrix0 = rmv_num(matrix0, num)
        rtn1 = bingo_combo(orig[mtx_n], all[mtx_n], check_rows(matrix0),num)
        rtn2 = bingo_combo(orig[mtx_n], all[mtx_n], check_colums(matrix0),num)
        if rtn1 or rtn2:
            exit()

