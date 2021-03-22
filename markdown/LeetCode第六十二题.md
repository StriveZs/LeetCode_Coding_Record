---
title: LeetCode No.62

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第六十二题
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

![figure.1](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

```
示例 1：

输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109
```
## 代码
```
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        核心思想：
                看到这道题，如果学过动态规划的话，肯定会首先想到使用动态规划来解
                根据题目内容来定义dp[i][j]
                这里的dp[i][j]表示从左上角到达(i,j)位置最多路径数
                动态规划解法:
                    定义 f[i][j] 为到达位置 (i,j) 的不同路径数量。
                    那么 f[n-1][m-1] 就是我们最终的答案，而 f[0][0] = 1 是一个显而易见的起始条件。
                    由于题目限定了我们只能 往下 或者 往右 移动，因此我们按照当前可选方向进行分析：
                        1.当前位置只能往下移动，即有 f[i][j] = f[i-1][j] (边界)
                        2.当前位置只能往右移动，即有 f[i][j] = f[i][j-1] (边界)
                        3.当前位置即能往下也能往右移动，即有 f[i][j] = f[i][j-1] + f[i-1][j]

        """
        dp = [[0 for i in range(n)] for i in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                # 既能往下也能往右移动
                if i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] # 非边界位置，因此它可以是从上边来的，可以是从左边来的
                elif i > 0: # 位于左边界  从上一个点过来只能往下走
                    dp[i][j] = dp[i-1][j]
                elif j > 0: # 位于上边界 从上一个点过来只能往右走
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(m = 3, n = 7))
```