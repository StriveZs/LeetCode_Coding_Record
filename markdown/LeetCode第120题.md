---
title: LeetCode No.120

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第120题—三角形最小路径和
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

 

示例 1：

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
示例 2：

输入：triangle = [[-10]]
输出：-10
 

提示：

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 

进阶：

你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？

## 代码
```
import sys
class Solution(object):
    maxSum = sys.maxsize # 设置足底啊之
    def limit_dfs(self,triangle,j,iList,curSum,curDepth,depth):
        """
        :param triangle: List[List[Int]] 所有数值
        :param j: Int 上一个节点的纵坐标
        :param iList: List[Int] 当前节点所在的层
        :param curParam: Int 当前层之前的路径和
        :param curDepth: Int 当前深度
        :param depth: 最大深度
        :return:
        """
        t = iList[j]
        curSum += iList[j]
        if depth == curDepth:
            if curSum < self.maxSum:
                self.maxSum = curSum
            return
        self.limit_dfs(triangle, j, triangle[curDepth+1], curSum, curDepth+1, depth)
        if j+1 < len(triangle[curDepth+1]):
            self.limit_dfs(triangle, j+1, triangle[curDepth + 1], curSum, curDepth+1, depth)
    # 超时版本
    def minimumTotal(self, triangle):
        """
        核心思想:
            每个节点，只能访问它的[i+1][j]/[i+1][j+1] 两个节点
            考虑采用递归来判断, 有点类似限制二叉树的访问方法
        :type triangle: List[List[int]]
        :rtype: int 返回最大值
        """
        self.limit_dfs(triangle,0,triangle[0],0,0,len(triangle)-1)
        return self.maxSum
    
    # 参考大佬的版本
    def new_version(self,triangle):
        for i in range(len(triangle) - 1, 0, -1):
            for j in range(i):
                triangle[i - 1][j] += min(triangle[i][j], triangle[i][j + 1])
        return triangle[0][0]


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([[-1],[2,3],[1,-1,-3]]))
```