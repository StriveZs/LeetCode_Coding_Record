import re

class Solution(object):
    def cut(self, str1):
        """
        得到字符串的所有子串
        :type str1: str
        :return: list
        """
        results = []
        # x + 1 表示子字符串长度
        for x in range(len(str1)):
            # i 表示偏移量
            for i in range(len(str1) - x):
                tempStr = str1[i:i + x + 1]
                results.append(tempStr)
        return results


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        split_res = self.cut(s)
        length = len(split_res)
        maxlen = 0
        result = ''
        for i in range(length):
            temp = split_res[length - i - 1][::-1] # 字符串翻转
            if temp == split_res[length - i - 1]:
                if len(temp) > maxlen:
                    maxlen = len(temp)
                    result = split_res[length - i - 1]

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('babad'))