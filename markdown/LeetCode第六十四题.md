---
title: LeetCode No.64

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第六十四题
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)
## 题目描述
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

![figure.1](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)

```
示例 1：

输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
```

## 代码
```
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        核心思想：
                看到这个题目的瞬间我就想起用动态规划了
                dp[i][j] 表示从(0,0)位置到当前位置的最短距离
                初始dp距离要设置的足够大

                分成三种情况：
                    1. 不位于边界的情况，可以从上过来，也可以从左过来，因此都要判断
                    2. 位于左边界的情况，只能从上过来
                    3. 位于上边界的情况，只能从左过来
        """

        dp = [[100000 for i in range(len(grid[0]))] for i in range(len(grid))] # 初始化dp
        dp[0][0] = grid[0][0]
        #print(len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j]+grid[i][j],dp[i][j])  # 非边界位置，因此它可以是从上边来的，可以是从左边来的
                    dp[i][j] = min(dp[i][j-1] + grid[i][j], dp[i][j])
                elif i > 0:  # 位于左边界  从上一个点过来只能往下走
                    dp[i][j] = min(dp[i-1][j]+grid[i][j],dp[i][j])
                elif j > 0:  # 位于上边界 从上一个点过来只能往右走
                    dp[i][j] = min(dp[i][j-1] + grid[i][j], dp[i][j])

        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum(grid = [[8,2,6,3,8,4,8,6,1,1,1,8,0],[1,6,0,6,7,1,2,4,7,8,9,3,8],[9,9,7,8,4,7,3,3,2,3,7,1,9],[8,4,3,8,6,4,4,7,2,3,0,4,8],[7,4,9,3,4,0,2,3,9,7,2,4,0],[7,7,9,0,9,9,4,2,7,0,8,3,9],[0,9,9,6,9,9,2,8,2,8,8,4,2],[9,3,4,3,5,1,3,4,1,2,3,7,4],[2,8,4,8,9,6,7,9,4,6,8,8,4],[2,6,4,8,8,4,2,5,9,9,6,4,4],[0,6,9,7,2,4,7,6,2,9,2,1,8],[8,7,8,6,3,0,3,9,8,3,5,2,8],[5,2,7,9,8,9,8,9,6,0,5,6,9],[7,5,3,8,5,2,7,5,8,2,7,3,2],[7,7,7,0,5,4,4,2,6,4,1,4,3],[0,6,9,8,5,8,5,1,9,2,3,8,7],[3,1,4,7,3,1,4,2,3,1,7,7,6]]))
```