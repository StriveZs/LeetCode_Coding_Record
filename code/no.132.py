class Solution(object):
    # fixme:判断是否是回文串
    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        return False
    # fixme:回溯法超时版本
    def time_out(self, s):
        """
        最终的结果，每个字符单独拿出来肯定是一个回文串, 因此不存在空字符串结果的情况，除非输入就是空串
        算法考虑的话，有两种方法:
            1. 动态规划
            2. 回溯法
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        # 回溯法
        def backtrack(s, res, path):
            if not s:
                res.append(len(path))
                return
            for i in range(1, len(s) + 1):  # 注意起始和结束位置
                if self.isPalindrome(s[:i]):
                    backtrack(s[i:], res, path + [s[:i]])
        backtrack(s,res,[])
        return min(res)-1

    # fixme:动态规划版本
    def minCut(self, s):
        dp = [i for i in range(len(s))] # 创建dp数组  0-len(s)-1 最少划分0次最多都划分完
        for i in range(len(s)):
            for j in range(i+1):
                temp = s[j:i+1]
                # 如果是回文串
                if temp == temp[::-1]:
                    if j > 0:
                        dp[i] = min(dp[i], dp[j - 1] + 1)
                    else:
                        dp[i] = 0
        return dp[len(s) - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.minCut("aab"))