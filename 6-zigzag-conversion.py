class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        diag_nums = numRows - 2
        res_rows = {key: "" for key in range(numRows)}
        vertical = []
        diagonal = []

        while s:
            main_part = s[:numRows]
            s = s[numRows:]
            diag_part = s[:diag_nums]
            s = s[diag_nums:]

            for idx, el in enumerate(main_part):
                res_rows[idx] += el

            for idx, el in enumerate(diag_part):
                row_idx = numRows - idx - 2
                res_rows[row_idx] += el

        return "".join(res_rows.values())
