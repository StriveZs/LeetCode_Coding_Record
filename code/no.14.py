import re

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        if strs[0] == '':
            return ""
        commanForward = ''
        flag = False
        index = -1
        for i in range(len(strs[0])):
            commanForward += strs[0][i]
            j = 1
            while j < len(strs):
                if commanForward != strs[j][0:i+1]:
                    index = i
                    flag = True
                    break
                j += 1
            if flag:
                break
            if ~flag:
                index = i+1
        if index == -1:
            return ""
        else:
            return strs[0][0:index]

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["a","a","b"]))
