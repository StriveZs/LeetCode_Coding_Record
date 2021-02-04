class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        核心思想：使用动态规划求解问题
                碰到")" 为基础长度为2
                内部连在一起的的长度为dp[i-1]
                外部连在一起的长度为dp[i-dp[i-1]-2]
                状态转移方程为：2 + dp[i-1] + dp[i-dp[i-1]-2]
        """
        length = len(s)
        if length == 0:
            return 0
        dp = [0] * length
        for i in range(1,length):
        	# 当遇到右括号时，尝试向前匹配左括号
            if s[i] == ')':
                pre = i - dp[i-1] -1
                # 如果是左括号，则更新匹配长度
                if pre >= 0 and s[pre] == '(':
                    dp[i] = dp[i-1] + 2
                    # 处理独立的括号对的情形 类似()()、()(())
                    if pre > 0:
                        dp[i] += dp[pre-1]
        return max(dp)
    
if __name__ == '__main__':
    s = Solution()
    print(s.longestValidParentheses(s = "()(())))"))