"""
Программа решает судоку (потому что мне лень думать)

На вход подаются числа подряд, между строками - пробел, вместо пропуска - '0'

Собственность @vlad.ostas :-)
"""
from cell import Cell


def show_field():
    for num_l, row in enumerate(sudoku_field):
        for num_d, value in enumerate(row):
            if (num_d + 1) % 3 == 0:
                print(value.digit, end='   ')
            else:
                print(value.digit, end='  ')
        print()
        if (num_l + 1) % 3 == 0:
            print()


def show_possibles():
    for num_l, row in enumerate(sudoku_field):
        for num_d, value in enumerate(row):
            if (num_d + 1) % 3 == 0:
                print(value.possibles(), end='   ')
            else:
                print(value.possibles(), end='  ')
        print()
        if (num_l + 1) % 3 == 0:
            print()


def edit_cell_surr(i, j, value):
    for k in range(len(sudoku_field)):
        sudoku_field[i][k].remove_possible(value)
        sudoku_field[k][j].remove_possible(value)
    rel_i, rel_j = i % 3, j % 3
    for chunk_i in range(i - rel_i, i + 3 - rel_i):
        for chunk_j in range(j - rel_j, j + 3 - rel_j):
            sudoku_field[chunk_i][chunk_j].remove_possible(value)


def check():
    for i, row in enumerate(sudoku_field):
        for j, cell in enumerate(row):
            if cell.digit > 0:
                edit_cell_surr(i, j, cell.digit)


def solve():  # TODO improve this function
    while True:
        _i_, _j_ = 0, 0
        _cell_ = 0
        can_solve = False
        for i, row in enumerate(sudoku_field):
            if can_solve:
                break
            for j, cell in enumerate(row):
                if len(cell.possibles()) == 1:
                    can_solve = True
                    _i_, _j_ = i, j
                    _cell_ = cell.possibles()[0]
                    break
        if not can_solve:
            break
        edit_cell_surr(_i_, _j_, _cell_)
        sudoku_field[_i_][_j_].digit = _cell_


solved = '534678912 672195348 198342567 859761423 426853791 713924856 961537284 287419635 345286179'
unsolved = '530070000 600195000 098000060 800060003 400803001 700020006 060000280 000419005 000080079'
sudoku_input = input().split()  # 9x9
sudoku_field = []
for i, line in enumerate(sudoku_input):
    sudoku_field.append([Cell(int(digit), i // 3 + (j // 3) * 3) for j, digit in enumerate(line)])
check()
solve()
show_field()
print()
show_possibles()
