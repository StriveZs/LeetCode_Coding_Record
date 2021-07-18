---
title: LeetCode No.145

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第145题—二叉树的后序遍历
回家休息几天，搬宿舍心累。再回实验室就开始好好科研了！！！

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
v给定一个二叉树，返回它的 后序 遍历。
```
示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
```

## 代码
```
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    res = []
    # fixme: 后序遍历
    def backward(self, node):
        if node is not None:
            self.backward(node.left)
            self.backward(node.right)
            self.res.append(node.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.backward(root)
        return self.res
```