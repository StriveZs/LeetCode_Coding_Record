---
title: LeetCode No.101

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第101题—对称二叉树
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个二叉树，检查它是否是镜像对称的。
```
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 
进阶：

你可以运用递归和迭代两种方法解决这个问题吗？
```

## 代码
一遍AC，思路很简单。就是效率不行。
```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isMirror(self,node1,node2):
        if node1 != None and node2 == None:
            return False
        elif node1 == None and node2 != None:
            return False
        elif node1 != None and node2 != None:
            if self.isMirror(node1.left, node2.right) == False:
                return False
            if node1.val != node2.val:
                return False
            if self.isMirror(node1.right,node2.left) == False:
                return False
            return True
        else:
            return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        核心思想：
            方法①：直接中序遍历，将得到的结果，如果得到序列是对称的则证明是镜像对称的 这种方法太蠢了
            方法②：直接使用递归一边遍历左子树，一边遍历右子树，左边采用中序遍历进行，右边的话采用镜像中序遍历的方法进行遍历即可
        """
        return self.isMirror(root,root)

```