---
title: LeetCode No.100

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第一百题—相同的数
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

![figure.1](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

```
示例 1：

输入：p = [1,2,3], q = [1,2,3]
输出：true
```

![figure.2](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

```
示例 2：
输入：p = [1,2], q = [1,null,2]
输出：false
```

![figure.3](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

```
示例 3：
输入：p = [1,2,1], q = [1,1,2]
输出：false
 

提示：

两棵树上的节点数目都在范围 [0, 100] 内
-104 <= Node.val <= 104
```

## 代码
执行用时：36 ms, 在所有 Python3 提交中击败了84.05%的用户内存消耗：14.9 MB, 在所有 Python3 提交中击败了53.64%的用户. 刷题的第100个，每天都在坚持，希望自己博士毕业能够把所有题刷完。

代码难得一遍AC

```
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def middle_search(self,node1,node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None and node2 != None:
            return False
        elif node1 != None and node2 == None:
            return False
        else:
            if self.middle_search(node1.left,node2.left) == False:
                return False
            if node1.val != node2.val:
                return False
            if self.middle_search(node1.right, node2.right) == False:
                return False
            return True
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        
        核心思想：
                同时对两个棵树进行先序遍历、中序遍历、后序遍历都可以，执行DFS就行了，然后同时比较结果，
            如果存在不同的情况，则返回False
        """
        return self.middle_search(p,q)
```