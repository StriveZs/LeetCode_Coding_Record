---
title: LeetCode No.44

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第四十四题
鸽了好几天我胡汉三又回来了。接着坚持，前段时间基金给我搞炸了裂开。  

## 题目描述
定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false

## 核心思想
这是经典的动态规划算法。  

首先是创建一个s和p对应的棋盘(dp)：

![figure.1](https://pic.leetcode-cn.com/a319e64f7824ab0590ef1dbaa016d6e47f22c631424b124cb1ecea842ba002c8-gaitubao_%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202020-07-05%20%E4%B8%8B%E5%8D%882.09.44.png)

然后对于*的情况，它理论上可以占据一行的True，但实际上是从它顶上的True开始占据后半行:

![figure.2](https://pic.leetcode-cn.com/c97b033d8e3f45686f87a3264404177411ac8095201c07c3e1af0b25953067b0-gaitubao_%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202020-07-05%20%E4%B8%8B%E5%8D%882.20.13.png)

然后对于？的情况，它则是从dp[i-1][j-1]变到dp[i][j]

![figure.3](https://pic.leetcode-cn.com/abee7c42685e277f93c1693447d403044e30a33d1a90f763a96d3373ed66ce2f-gaitubao_%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202020-07-05%20%E4%B8%8B%E5%8D%882.44.25.png)

下面是我参考大佬的代码。

## 代码
```
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool

        核心思想：使用动态规划
                构建一个 len(s)+1 * len(p)+1 的dp动态矩阵
                加1是因为：考虑s或p为空的情况下的初始状态
        """
        line = len(p) + 1 # 行
        row = len(s) + 1 # 列
        # 创建dp数组
        dp = [[False]*row for _ in range(line)]
        dp[0][0] = True

        # 单独处理s为空的情况
        if s == "":
            for i in range(len(p)):
                if p[i] != '*':
                    return False
            return True

        # 单独处理p以*开头的情况
        if p.startswith('*'):
            dp[1] = [True]*row

        # 开始处理
        for i in range(1,line):
            isAsterisk = False # 是否为 *
            for j in range(1,row):
                # 处理相等的情况
                if s[j-1] == p[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                # 处理 ? 的情况
                elif p[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                # 处理 * 的情况
                elif p[i-1] == '*':
                    # 处理前面已经出现*的情况或者pattern以*开头的情况
                    if dp[i-1][0] == True:
                        dp[i] = [True] * row
                    # 处理顶上为True下一个出现*的情况
                    if dp[i-1][j]:
                        isAsterisk = True
                    # 从该True位置开始后面该行均为True
                    if isAsterisk:
                        dp[i][j] = True

        # 返回结果
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.isMatch(s = "",p = "**a**"))
```