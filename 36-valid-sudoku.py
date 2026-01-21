board = [
    ["1", ".", "1", "2", ".", "2", "3", ".", "3"],
    [".", "1", ".", ".", "2", ".", ".", "3", "."],
    ["1", ".", "1", "2", ".", "2", "3", ".", "3"],
    ["4", ".", "4", "5", ".", "5", "6", ".", "6"],
    [".", "4", ".", ".", "5", ".", ".", "6", "."],
    ["4", ".", "4", "5", ".", "5", "6", ".", "6"],
    ["7", ".", "7", "8", ".", "8", "9", ".", "9"],
    [".", "7", ".", ".", "8", ".", ".", "9", "."],
    ["7", ".", "7", "8", ".", "8", "9", ".", "9"],
]


# [".",".","."|".","5","."|"6","1","."]
# [".","4","."|"3",".","."|".",".","."]
# [".",".","."|"2",".","6"|".",".","1"]
# ["8",".","."|".",".","."|".","2","."]
# [".",".","2"|".","7","."|".",".","."]
# [".","1","5"|".",".","."|".",".","."]
# [".",".","."|".",".","2"|".",".","."]
# [".","2","."|"9",".","."|".",".","."]
# [".",".","4"|".",".","."|".",".","."]


def isValidSudoku(board) -> bool:
    rows = {key: [] for key in range(9)}
    columns = {key: [] for key in range(9)}
    triplets = {key: [] for key in range(1, 10)}
    row_shift = 0
    col_shift = 0
    for row_idx, row in enumerate(board):
        for col_idx, el in enumerate(row):
            if el in rows[row_idx] or el in columns[col_idx]:
                return False
            if el != ".":
                rows[row_idx].append(el)
                columns[col_idx].append(el)
                print(col_idx + 1, row_idx + 1, el)
                # triangle = (col_idx + row_idx + 2) // 3
                if col_idx > row_idx + 1:
                    triangle = (col_idx // 3) + 1
                    print(triangle)
                    triplets[triangle].append(el)
                elif col_idx + 1 < row_idx:
                    triangle = (col_idx // 3) + 2
                    print(triangle)
                    triplets[triangle + 2].append(el)
                else:
                    if col_idx > row_idx:
                        triangle = (col_idx // 3) + 1
                    elif col_idx < row_idx:
                        triangle = (col_idx // 3) + 2
                    else:
                        triangle = (col_idx + row_idx + 2) // 3
                    print(triangle)
                    triplets[triangle].append(el)

    print(triplets)

    return True

    # print(rows)
    # print(columns)


print(isValidSudoku(board))
