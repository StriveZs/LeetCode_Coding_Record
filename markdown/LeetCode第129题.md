---
title: LeetCode No.129

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第129题—求根节点到叶节点数字之和
好久没更新了，最近事情太多了，天天忙的要死，英语也没来得及背，后面会慢慢恢复的，同时也会更新一大堆学习到的东西，敬请期待。  

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。

![figure.1](https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg)

```
示例 1：

输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25
```

![figure.2](https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg)

```
示例 2：
输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026
 
提示：

树中节点的数目在范围 [1, 1000] 内
0 <= Node.val <= 9
树的深度不超过 10
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
    sum = 0
    def dfs(self, node, curStr):
        if node != None:
            curStr += str(node.val)
            if node.right == None and node.left == None:
                self.sum += int(curStr)
            self.dfs(node.left, curStr)
            self.dfs(node.right, curStr)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int

        D FS 强制类型转换并且记录就好了
        """
        self.sum =0
        self.dfs(root, '')
        return self.sum

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    root.left = node1
    root.right = node2
    print(s.sumNumbers(root))
```