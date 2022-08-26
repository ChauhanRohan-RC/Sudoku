import time

""" A Sudoku Solver Program using BACK_TRACK Algorithm """

# Constants
VERSION = 1.0
VOID = 0  # should be different from input_range
BOARD_SIZE = 9
BOX_SIZE = 3
INPUT_RANGE = (1, 10)  # from 1st to last excluding last


def check(_board, pos: tuple, num: int) -> bool:
    """
      Returns if the attempted move is valid

      :param _board: Sudoku board: (2d list of ints)
      :param pos: position to check: Tuple in form (row, col)
      :param num: number to check on given position: int
      :return: bool
      """

    # check row
    for i in range(len(_board[0])):
        if _board[pos[0]][i] == num and i != pos[1]:
            return False

    # check column
    for j in range(len(_board)):
        if _board[j][pos[1]] == num and j != pos[0]:
            return False

    # check box
    bx = pos[1] // BOX_SIZE
    by = pos[0] // BOX_SIZE

    for i in range(bx * BOX_SIZE, bx * BOX_SIZE + BOX_SIZE):
        for j in range(by * BOX_SIZE, by * BOX_SIZE + BOX_SIZE):
            if _board[j][i] == num and (j, i) != pos:
                return False

    return True


def find_void(_board):
    """
    finds an empty spot in the board

    :param _board: Sudoku board: (2d list of ints)
    :return: position of empty spot: (row, col)
    """
    for i in range(len(_board)):
        for j in range(len(_board[0])):
            if _board[i][j] == VOID:
                return i, j
    return None


def solve(_board) -> bool:
    """
    Solves a sudoku board using BACK-TRACK ALGORITHM
    :param _board: Sudoku board: (2d list of ints)
    :return: True if solved else False
    """
    void_pos = find_void(_board)
    if not void_pos:
        return True

    row, col = void_pos
    for i in range(INPUT_RANGE[0], INPUT_RANGE[1]):
        if check(_board, void_pos, i):
            _board[row][col] = i

            if solve(_board):           # recursive BACK-TRACK call
                return True

            _board[row][col] = VOID     # reset this pos
    return False


def get_string(_board) -> str:
    """
    creates string representation of Sudoku board

    :param _board: Sudoku board: (2d list of ints)
    :return: string representation of Sudoku board
    """

    bo_str = ''
    for i in range(len(_board)):
        if i != 0 and i % BOX_SIZE == 0:
            bo_str += ('-' * (BOARD_SIZE + BOX_SIZE) * 2) + '-\n'
        for j in range(len(_board[0])):
            if j % BOX_SIZE == 0:
                bo_str += '| '
            bo_str += str(_board[i][j]) + (' |\n' if j == BOARD_SIZE - 1 else ' ')
    return bo_str


def start_solve(_board):
    print(f'\n.................. VERSION : RC {VERSION} ....................\n')
    s_ = time.time()
    solve(_board)
    e_ = time.time()
    print(get_string(_board))
    print(f'\nSolved in {e_ - s_} seconds')


if __name__ == '__main__':    
    board = [
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [8, 0, 9, 0, 7, 1, 0, 2, 0],
        [4, 0, 3, 5, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 0, 7],
        [0, 0, 2, 0, 3, 4, 0, 8, 0],
        [7, 3, 0, 0, 0, 9, 0, 0, 4],
        [9, 0, 0, 0, 0, 0, 7, 0, 2],
        [0, 0, 8, 2, 0, 5, 0, 9, 0],
        [1, 0, 0, 0, 4, 0, 3, 0, 0]
    ]

    start_solve(board)
