---
title: LeetCode No.103

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第103题—二叉树的锯齿形层序遍历
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
```
例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
```

## 代码
比较懒直接把上一题的结果，拿过来，将偶数层逆序就好了。
```
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    res = dict()  # 用字典存储对应深度的结果
    def forwardSearch(self, root, depth):
        if root != None:
            if depth not in self.res.keys():
                self.res[depth] = []
            self.res[depth].append(root.val)
            self.forwardSearch(root.left, depth + 1)
            self.forwardSearch(root.right, depth + 1)

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        核心思想：
            类似上一题的方法，先得到层序的结果
            然后将深度为偶数的结果倒序就好了
        """
        self.res = dict()
        self.forwardSearch(root, 1)
        result = []
        for i in self.res.keys():
            if i % 2 == 0:
                result.append(self.res[i][::-1])
            else:
                result.append(self.res[i])
        return result

if __name__ == '__main__':
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    root.left = node1
    root.right = node2
    node1.left = node3
    node2.right = node4
    s = Solution()
    print(s.zigzagLevelOrder(root))
```