---
title: LeetCode No.99

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第九十九题—恢复二叉搜索树
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。

进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？

![figure.1](https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg)
 
```
示例 1：

输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
```

![figure.2](https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg)

```
示例 2：
输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
 

提示：

树上节点的数目在范围 [2, 1000] 内
-231 <= Node.val <= 231 - 1
```

## 代码
```
# Definition for a binary tree node.
import sys
import copy
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    errorNode1 = TreeNode() # 记录错误节点1
    errorNode2 = TreeNode() # 记录错误节点2
    pre = TreeNode(-sys.maxsize) # 记录前一个值
    flag = True
    def middleSearch(self,node):
        if node == None:
            return
        self.middleSearch(node.left) # 访问左子树
        if self.pre.val > node.val and self.pre.val != -sys.maxsize: # 这里的-sys.maxsize是一个最小值
            if self.flag:
                self.errorNode1 = self.pre # 由于当前节点小于上一个节点，因此记录上一个节点比如：321 应该是记录3
                self.flag = False
            self.errorNode2 = node # 如321，记录完3之后应该记录1，所以是记录当前node
        self.pre = node
        self.middleSearch(node.right) # 访问右子树

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.

        核心思想：
            依然是采用中序遍历，并记录两个错误顺序的点，最后进行交换
        """
        self.middleSearch(root)
        print(self.errorNode1.val, self.errorNode2.val)
        temp = self.errorNode1.val
        self.errorNode1.val = self.errorNode2.val
        self.errorNode2.val = temp


if __name__ == '__main__':
    root = TreeNode(5)
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(-2147483648)
    node4 = TreeNode(2)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    s = Solution()
    s.recoverTree(root)
```