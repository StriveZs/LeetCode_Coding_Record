class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        核心思想: 迭代思想，就是从头往后依次找到n相等的那种情况返回（重点是读懂题目）

        """
        if n == 1:
            return str(1)
        s = "1"
        for i in range(n-1):
            t = ""
            i, j = 0, len(s)
            count = 1 # 统计相同个数
            while i < j-1:
                if s[i] == s[i+1]:
                    count += 1
                    i += 1
                else:
                    # 重新统计
                    t = t + str(count) + s[i]
                    count = 1
                    i += 1
            s = t + str(count) + s[i]
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(4))
