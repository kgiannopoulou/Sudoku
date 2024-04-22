def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty_location(board, loc):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                loc[0], loc[1] = row, col
                return True
    return False


def used_in_row(board, row, num):
    return num in board[row]


def used_in_col(board, col, num):
    return num in [board[i][col] for i in range(9)]


def used_in_box(board, row, col, num):
    start_row, start_col = row - row % 3, col - col % 3
    return any(num == board[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3))


def is_safe(board, row, col, num):
    return not used_in_row(board, row, num) and not used_in_col(board, col, num) and not used_in_box(board, row, col, num)


def solve_sudoku(board):
    loc = [0, 0]

    if not find_empty_location(board, loc):
        return True

    row, col = loc[0], loc[1]

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


if __name__ == "__main__":
    # Example board
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(board):
        print("Sudoku solved successfully:")
        print_board(board)
    else:
        print("No solution exists")
