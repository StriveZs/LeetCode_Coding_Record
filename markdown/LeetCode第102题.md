---
title: LeetCode No.102

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第102题—二叉树的层序遍历
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

```
示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
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
    res = dict() # 用字典存储对应深度的结果
    def forwardSearch(self,root,depth):
        if root != None:
            if depth not in self.res.keys():
                self.res[depth] = []
            self.res[depth].append(root.val)
            self.forwardSearch(root.left,depth+1)
            self.forwardSearch(root.right,depth+1)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        核心思想：
            采用前序遍历，这样的话会先访问根节点，再访问左节点，最后再访问右节点
            对于例题中的例子:
                    3
                   / \
                  9  20
                    /  \
                   15   7
        前序遍历的结果正好就是 3 9 20 15 7
        只需要添加depth就可以区分深度了
        """
        self.forwardSearch(root,1)
        result = []
        for i in self.res.keys():
            result.append(self.res[i])
        return result

if __name__ == '__main__':
    root = TreeNode(1)

    s = Solution()
    print(s.levelOrder(root))
```