---
title: LeetCode No.32

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第三十二题
## 题目描述
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

 
```
示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0
 

提示：

0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'
```

## 代码
```
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
```