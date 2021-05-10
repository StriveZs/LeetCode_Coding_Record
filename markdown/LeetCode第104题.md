---
title: LeetCode No.104

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第104题—二叉树的最大深度
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。
```
示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 
```

## 代码
执行用时：24 ms, 在所有 Python 提交中击败了92.24%的用户内存消耗：15.5 MB, 在所有 Python 提交中击败了85.16%的用户 深度遍历DFS，求深度

```
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    maxdepth = 0
    def dfs_depth(self,node,depth):
        if node != None:
            self.dfs_depth(node.left,depth+1)
            if depth > self.maxdepth:
                self.maxdepth = depth
            self.dfs_depth(node.right,depth+1)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        核心思想：
            dfs遍历最大深度，效果最差
        """
        self.dfs_depth(root,1)
        return self.maxdepth

```