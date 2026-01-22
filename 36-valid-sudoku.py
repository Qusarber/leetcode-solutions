class Solution(object):
    def isValidSudoku(self, board):
        rows = {key: [] for key in range(9)}
        columns = {key: [] for key in range(9)}
        triplets = {key: [] for key in range(9)}
        triangles = {
            "0-0": 0,
            "1-0": 1,
            "2-0": 2,
            "0-1": 3,
            "1-1": 4,
            "2-1": 5,
            "0-2": 6,
            "1-2": 7,
            "2-2": 8,
        }
        for row_idx, row in enumerate(board):
            for col_idx, el in enumerate(row):
                triangle = triangles["{}-{}".format(col_idx // 3, row_idx // 3)]
                if (
                    el in rows[row_idx]
                    or el in columns[col_idx]
                    or el in triplets[triangle]
                ):
                    return False
                if el != ".":
                    rows[row_idx].append(el)
                    columns[col_idx].append(el)
                    triplets[triangle].append(el)
        return True
