---
title: LeetCode No.119

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第119题—杨辉三角II
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

![fiogure.1](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

在杨辉三角中，每个数是它左上方和右上方的数的和。
```
示例:

输入: 3
输出: [1,3,3,1]
```

## 代码
```
class Solution(object):
    res = []  # 全局结果

    # fixme: 递归分治生成数组
    def genrate_iList(self, pre_list, depth, goal_depth):
        """
        采用递归分治的方法来生成每一层的数组
        :param pre_list: List 上一层生成的数组
        :param depth: Int 当前深度
        :param goal_depth: Int 目标深度
        :return:
        """
        if depth == goal_depth + 1:
            return
        temp = []
        temp.append(1)
        for i in range(len(pre_list) - 1):
            temp.append(pre_list[i] + pre_list[i + 1])
        temp.append(1)
        self.res.append(temp)

        # 递归调用
        self.genrate_iList(temp, depth + 1, goal_depth)

    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]

        核心思想：
            由于每个值都是它上面两个值的加和，因此考虑为分治问题
            考虑还是使用递归的方法，因此每次传入的数组就是上一次递归生成的数组.
        """
        self.res = []
        if numRows == 0:
            return self.res
        self.res.append([1])
        if numRows == 1:
            return self.res
        self.res.append([1, 1])
        if numRows == 2:
            return self.res
        self.genrate_iList([1, 1], 3, numRows+1)
        return self.res[-1]
```