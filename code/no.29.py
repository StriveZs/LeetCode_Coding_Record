class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        i, a, b = 0, abs(dividend), abs(divisor)
        # 被除数小于除数的情况直接返回0
        if a == 0 or a < b:
            return 0

        while b <= a:
            b = b << 1  # 位运算 位左移1位
            i = i + 1  # i为2幂
        else:
            res = (1 << (i - 1)) + self.divide(a - (b >> 1), abs(divisor)) # 用减法来得到商
            if (dividend ^ divisor) < 0: # 负结果判断
                res = -res
            return min(res, (1 << 31) - 1) # 去掉溢出情况
