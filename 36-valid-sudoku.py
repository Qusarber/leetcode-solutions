board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "4", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]


# [".",".","."|".","5","."|".","1","."]
# [".","4","."|"3",".","."|".",".","."]
# [".",".","."|".",".","4"|".",".","1"]
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
                print(row_idx, col_idx, el)
                trinangle = (col_idx + row_idx + 2) // 3
                print(trinangle)
                if col_idx > row_idx + 1:
                    triplets[trinangle].append(el)
                elif col_idx + 1 < row_idx:
                    triplets[trinangle + 2].append(el)
                else:
                    triplets[trinangle].append(el)

    print(triplets)

    return True

    # print(rows)
    # print(columns)


print(isValidSudoku(board))
