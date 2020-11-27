import random
import copy

DIGITS = [
    1, 2, 3, 4, 5, 6, 7, 8, 9
]

RAW = 9
COL = 9


def generate_four_cross_num(center_num):
    x = copy.deepcopy(DIGITS)
    x.remove(center_num)

    y = copy.deepcopy(x)
    first_num = random.choice(y)
    y.remove(first_num)
    fourth_num = random.choice(y)

    z = copy.deepcopy(x)
    second_num = random.choice(z)
    z.remove(second_num)
    third_num = random.choice(z)
    return first_num, second_num, third_num, fourth_num


def generate_four_conner_num(first_cross, second_cross, third_cross, forth_cross):
    first = [first_cross, second_cross]
    first_conner = random.choice(list(set(DIGITS) - set(first)))

    second = [first_conner, first_cross, third_cross]
    second_conner = random.choice(list(set(DIGITS) - set(second)))

    third = [first_conner, second_cross, forth_cross]
    third_conner = random.choice(list(set(DIGITS) - set(third)))

    forth = [second_conner, third_cross, third_conner, forth_cross]
    forth_conner = random.choice(list(set(DIGITS) - set(forth)))

    return first_conner, second_conner, third_conner, forth_conner


def generate_sudoku_map():
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(RAW)
    ]

    sudoku[4][4] = random.choice(DIGITS)
    sudoku[1][4], sudoku[4][1], sudoku[4][7], sudoku[7][4] = generate_four_cross_num(sudoku[4][4])
    sudoku[1][1], sudoku[1][7], sudoku[7][1], sudoku[7][7] = generate_four_conner_num(sudoku[1][4], sudoku[4][1],
                                                                                      sudoku[4][7], sudoku[7][4])

    # for i, raw in enumerate(sudoku):
    #
    #     for j, col in enumerate(sudoku):
    #

    # todo
    for _ in sudoku:
        print(_)


sodu_map = generate_sudoku_map()
