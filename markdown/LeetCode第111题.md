---
title: LeetCode No.111

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第111题—二叉树的最小深度
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。

![figure.1](https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg)
 
```
示例 1：

输入：root = [3,9,20,null,null,15,7]
输出：2

示例 2：

输入：root = [2,null,3,null,4,null,5,null,6]
输出：5
 
提示：

树中节点数的范围在 [0, 105] 内
-1000 <= Node.val <= 1000
```

## 代码
执行用时：944 ms, 在所有 Python 提交中击败了18.01%的用户内存消耗：92.5 MB, 在所有 Python 提交中击败了61.96%的用户
```
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    globalMinDepth = 100000
    def depthSearch(self, node, depth):
        if node == None:
            return
        # 为叶子节点，进行深度判断
        if node.left == None and node.right == None:
            if depth < self.globalMinDepth:
                self.globalMinDepth = depth + 1 # +1的原因是因为这里的深度算当前的深度
            return
        self.depthSearch(node.left, depth+1)
        self.depthSearch(node.right, depth+1)
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        核心思想：
            最小深度是从根节点到最近叶子节点的最短路径上的节点数量
            使用DFS，设置一个全局最小深度，每当到达一个叶子结点就和当前全局最大深度进行比较
            要确保节点是叶子节点
            如果小于则更新全剧最小深度。
        """
        if root == None:
            return 0
        self.depthSearch(root,0)
        return self.globalMinDepth

if __name__ == '__main__':
    root = TreeNode(2)
    node1 = TreeNode(3)
    node2 = TreeNode(4)
    node3 = TreeNode(5)
    node4 = TreeNode(6)
    root.right = node1
    node1.right = node2
    node2.right = node3
    node3.right = node4
    s = Solution()
    print(s.minDepth(root))
```