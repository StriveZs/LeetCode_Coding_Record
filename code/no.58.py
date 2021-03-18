class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        核心思想:
                python方法直接用split(' ')对字符串进行划分，返回list[-1]的长度即可
                注意考虑全是空格的情况
        """
        res = s.split(' ')
        #print(res)
        for i in range(len(res)):
            if res[len(res)-i-1] != '':
                return len(res[len(res)-i-1])
        return 0
if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord(s = "     "))