---
title: LeetCode No.70

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第七十题—爬楼梯
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
```
示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
```

## 代码
```
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        核心思想：
                采用动态规划
                dp[i]表示爬到第i个阶梯所有需要的方法数
                题目分析（只考虑一步达到的情况）:
                    因为每次只能爬一个或者两个台阶
                    当处于i-1时则爬一阶可以从i-1爬到i
                    当处于i-2时则爬两阶可以从i-2爬到i
                    其余的情况均不能一步到达i
                综上所述：dp[i] =  dp[i-1] + dp[i-2]
        """
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))
```