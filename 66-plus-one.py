class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # solution 1:
        # num = int("".join(str(i) for i in digits)) + 1
        # return list(int(el) for el in str(num))

        res_l = []
        s = 0
        addable = 1

        for i in digits[::-1]:
            i = i + addable + s

            s = i // 10
            res = i % 10
            addable = 0

            res_l.append(res)

        if s:
            res_l.append(s)

        return res_l[::-1]
