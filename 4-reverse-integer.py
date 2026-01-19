class Solution(object):
    def reverse(self, x):
        if x >= 0:
            x = int(str(x)[::-1])
        else:
            x = int("-" + str(x)[::-1].replace("-", ""))

        if -(2**31) <= x <= 2**31 - 1:
            return x
        return 0
