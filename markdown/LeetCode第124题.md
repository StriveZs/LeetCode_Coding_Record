---
title: LeetCode No.123=4

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第123题—买卖股票的最佳时机III
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

![figure.1](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)

```
示例 1：

输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
```

![figure.2](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)

```
示例 2：

输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
 

提示：

树中节点数目范围是 [1, 3 * 104]
-1000 <= Node.val <= 1000
```
## 代码
```
import sys
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    max_sum = -sys.maxsize
    def dfs_statistic_path(self, root):
        if root == None:
            return 0
        left_sum = max(0, self.dfs_statistic_path(root.left)) # 统计左子树的路径总和
        right_sum = max(0, self.dfs_statistic_path(root.right)) # 统计右子树的路径总和
        temp = left_sum + root.val + right_sum # 统计当前路径总和
        self.max_sum = max(self.max_sum, temp) # 和当前最大路径进行比较
        return max(left_sum,right_sum) + root.val # 由于不能够返回(节点不能够重复)，因此只能选择出最大的一个子树再加上当前根节点值来返回

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        整体上是分而治之的思想，看成一个个子问题
        将每个节点看成是它子树的路径和(左子树和右子树)+他本来的值
        只有子路径和大于0的时候才会去统计它
        """
        self.dfs_statistic_path(root)
        return self.max_sum

if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2
    s = Solution()
    print(s.maxPathSum(root))
```