class Solution(object):
    def reverseWords(self, s):
        """
        使用split分割之后进行翻转即可
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        res = ''
        for i in range(len(s)):
            if s[len(s) - i - 1] == '':
                continue
            if res == '':
                res = s[len(s) - i - 1]
            else:
                res = res + ' ' + s[len(s) - i - 1]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("a good   example"))