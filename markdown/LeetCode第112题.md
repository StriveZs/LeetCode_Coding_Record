---
title: LeetCode No.112

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第112题—路径总和
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。

叶子节点 是指没有子节点的节点。

![figure.1](https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg)
 
```
示例 1：

输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
```

![figure.2](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

```
示例 2：

输入：root = [1,2,3], targetSum = 5
输出：false

示例 3：

输入：root = [1,2], targetSum = 0
输出：false
 
提示：

树中节点的数目在范围 [0, 5000] 内
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
```

## 代码
执行用时：44 ms, 在所有 Python3 提交中击败了94.71%的用户内存消耗：16.6 MB, 在所有 Python3 提交中击败了47.96%的用户
```
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    flag = False # 全局标志：表示是否存在一条路径数值加和等于目标值
    def sumPath(self, node, curSum, targetSum):
        """
        :param node: 当前节点
        :param curSum: 到当前节点之前的节点数值总和
        :param targetSum: 目标总和
        :return:
        """
        if node == None:
            return
        # 如果到达叶子节点，则进行总和判断
        if node.left == None and node.right == None:
            if curSum + node.val == targetSum:
                self.flag = True
        self.sumPath(node.left,curSum+node.val,targetSum)
        self.sumPath(node.right, curSum + node.val, targetSum)

    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool

        核心思想：
            采用DFS，每当遇到叶子结点，就去计算当前路径总和，如果等于targetSum就将全局标志flag设置为True
        """
        self.sumPath(root,0,targetSum)
        return self.flag
```