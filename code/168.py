#
# @lc app=leetcode.cn id=168 lang=python
#
# [168] Excel表列名称
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        思路：这是26进制计算法
        对columnNumber进行取余，余数查表就是结果
        :type columnNumber: int
        :rtype: str
        """
        num2chara = {
            1: 'A',
            2: 'B',
            3: 'C',
            4: 'D',
            5: 'E',
            6: 'F',
            7: 'G',
            8: 'H',
            9: 'I',
            10: 'J',
            11: 'K',
            12: 'L',
            13: 'M',
            14: 'N',
            15: 'O',
            16: 'P',
            17: 'Q',
            18: 'R',
            19: 'S',
            20: 'T',
            21: 'U',
            22: 'V',
            23: 'W',
            24: 'X',
            25: 'Y',
            26: 'Z'
            }
        res = ''
        while columnNumber > 26:
            remainder = columnNumber % 26
            if remainder == 0:
                res = num2chara[26] + res
                columnNumber = (columnNumber - 26) / 26
            else:
                res = num2chara[remainder] + res
                columnNumber = (columnNumber - remainder) / 26
        if columnNumber != 0:
            res = num2chara[columnNumber] + res
        return res

# s = Solution()
# print(s.convertToTitle(columnNumber = 701))

# @lc code=end

