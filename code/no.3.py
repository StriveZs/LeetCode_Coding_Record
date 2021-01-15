import re

class Solution(object):
    def noRepeat(self,str1):
        """
        判断字符串是否存在重复字符
        :param str1:
        :return: Bool
        """
        flag = True
        for i in range(len(str1)):
            l1 = re.findall(str1[i],str1)
            if len(l1) != 1:
                flag = False
        return flag

    def cut(self, str1):
        """
        得到字符串的所有子串
        :type str1: str
        :return: list
        """
        results = []
        num = 0
        # x + 1 表示子字符串长度
        for x in range(len(str1)):
            # i 表示偏移量
            for i in range(len(str1) - x):
                tempStr = str1[i:i + x + 1]
                if self.noRepeat(tempStr):
                    results.append(tempStr)
        return results

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # print(self.cut(s))
        split_str = self.cut(s)
        maxLen = 0
        for i in range(len(split_str)):
            pattern = split_str[i]
            if re.search(pattern,s) != None:
                if len(pattern) > maxLen:
                    maxLen = len(pattern)
        return maxLen
if __name__ == '__main__':
    s = "pwwkew"
    test1 = Solution()
    print(test1.lengthOfLongestSubstring(s))
    # print(test1.noRepeat('abc'))

