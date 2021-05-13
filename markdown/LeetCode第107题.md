---
title: LeetCode No.107

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第107题—二叉树的层序遍历II
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
```
例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层序遍历为：

[
  [15,7],
  [9,20],
  [3]
]
```

## 代码
魔改102题就好了。直接reverse.  
执行用时：40 ms, 在所有 Python3 提交中击败了76.52%的用户内存消耗：15.7 MB, 在所有 Python3 提交中击败了6.45%的用户
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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        核心思想：
            延续二叉树的层序遍历第一期的思想
            只不过是将最终得到的结果reverse就可以了。
            同样是采用前序遍历，按照深度进行划分，只不过是从最大深度开始存储就可以了
        """
        self.forwardSearch(root, 1)
        result = []
        self.dic = dict()
        for i in self.res.keys():
            result.append(self.res[i])
        return result[::-1]

if __name__ == '__main__':
    root = TreeNode(1)

    s = Solution()
    print(s.levelOrderBottom(root))
```