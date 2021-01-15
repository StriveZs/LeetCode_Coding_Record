class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False

        if x == 0:
            return x
        if x < 0:
            flag = True
            x = abs(x)
        item = list(str(x))
        item_reverse = item[::-1]
        result = ''
        for i in range(len(item_reverse)):
            result += item_reverse[i]
        result = int(result)
        if flag:
            result = -1 * result
        if result < -(2**31) or result > (2**31):
            return 0
        return result

if __name__ == '__main__':
    s = Solution()
    print(2**31)
    print(s.reverse(1534236469))
